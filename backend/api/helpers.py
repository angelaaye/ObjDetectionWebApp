import re
import json
import operator
import datetime

from database import db
from database.models import User
from database.models import Photo

from passlib.hash import pbkdf2_sha256

import os
import uuid
import glob
from PIL import Image
from config import config
from api.yolo import yolo_object_detection

def authenticate_user(username, password):
    print("Querying user tied to username and password")
    user = User.query.filter_by(username=username).first()
    if user and pbkdf2_sha256.verify(password, user.password):
        return user
    else:
        return None

def create_account(username, password):
	user = User.query.filter_by(username=username).first()
	if not user:  # username not taken
		last_user = User.query.order_by(User.id.desc()).first()
		# get a different salt for every unique user
		salt = last_user.id + 1 if last_user else 1
		user = User(
			username=username,
			password=pbkdf2_sha256.using(salt=bytes(salt), salt_size=16).hash(password)
		)
		db.session.add(user)
		db.session.commit()
		return user
	else:
		return None

def convert_to_thumbnail(filename):
	im = Image.open(os.path.join(config['UPLOAD_FOLDER'], filename))
	# convert to thumbnail image
	im.thumbnail((128, 128), Image.ANTIALIAS)
	# prefix thumbnail file with T_
	thumbnail_link = "T_" + filename
	im.save(os.path.join(config['UPLOAD_FOLDER'], thumbnail_link))
	return thumbnail_link

def upload_photo(id, photo):
	filename = photo.filename
	extension = filename.rsplit('.', 1)[1].lower()
	if '.' in filename and extension in {'png', 'jpg', 'jpeg'}:
		# random filename so that if a user uploads images with same filenames, they won't be overwritten
		new_filename = uuid.uuid4().hex + '.' + extension
		photo.save(os.path.join(config['UPLOAD_FOLDER'], new_filename))
		# get thumbnail link
		thumbnail_link = convert_to_thumbnail(new_filename)
		processed_link = yolo_object_detection(config['UPLOAD_FOLDER'], new_filename, config['UPLOAD_FOLDER'])
		# create new database record
		photo = Photo(
			user_id=id,
			thumbnail_link=thumbnail_link,
			photo_link=new_filename,
			processed_link=processed_link
		)
		db.session.add(photo)
		db.session.commit()
		return photo
	else:
		return None




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
	"""
	Given a username and password, check the database to see if the record exists.
	"""
	user = User.query.filter_by(username=username).first()
	if user and pbkdf2_sha256.verify(password, user.password):
	    return user
	else:
		return None

def create_account(username, password):
	"""
	Given a username, check if the username exists. If not, create a new account with password.
	"""
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
	"""
	Given an image, convert it to a thumbnail of maximum size 128 x 128.
	"""
	im = Image.open(os.path.join(config['UPLOAD_FOLDER'], filename))
	# convert to thumbnail image
	im.thumbnail((128, 128), Image.ANTIALIAS)
	# prefix thumbnail file with T_
	thumbnail_link = "T_" + filename
	im.save(os.path.join(config['UPLOAD_FOLDER'], thumbnail_link))
	return thumbnail_link

def upload_photo(id, photo):
	"""
	Given a photo, save it in the local drive, process the photo using yolov3 and finally
	convert the processed photo to a thumbnail photo and save it. 
	"""
	filename = photo.filename
	extension = filename.rsplit('.', 1)[1].lower()
	if '.' in filename and extension in {'png', 'jpg', 'jpeg'}:
		# random filename so that if a user uploads images with same filenames, they won't be overwritten
		new_filename = uuid.uuid4().hex + '.' + extension
		photo.save(os.path.join(config['UPLOAD_FOLDER'], new_filename))
		# process the image and return the filename
		processed_link = yolo_object_detection(config['UPLOAD_FOLDER'], new_filename, config['UPLOAD_FOLDER'])
		# get thumbnail of the processed image
		thumbnail_link = convert_to_thumbnail(processed_link)
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


def auth_photo_link(user, photo, photo_type):
	"""
	Retrieve a processed/thumbnail/original photo based on the input photo_type.
	"""
	mapping = {'T': photo.thumbnail_link, 'O': photo.photo_link, 'P': photo.processed_link}
	if user == photo.user_id:
		return os.path.join(config['UPLOAD_FOLDER'], mapping[photo_type])
	else:
		return os.path.join(config['UPLOAD_FOLDER'], '401.jpg')
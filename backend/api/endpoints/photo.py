from flask import request, jsonify, send_file
from flask_restplus import Resource, reqparse, abort
from api.restplus import api
from flask_jwt_extended import jwt_required, get_jwt_identity

from api.parsers import user_info, photo_upload, photo_info
from api.helpers import upload_photo
from api.serializers import photo_json
from database.models import Photo

import os
from config import config

ns = api.namespace('photo', description='APIs related to ECE1779A1 photo upload/view')

@ns.route('/')
class ThumbnailPhotos(Resource):
    @jwt_required
    @api.marshal_with(photo_json)
    def get(self):
        """
        Return uploaded photos as thumbnails from access token
        """
        current_user = get_jwt_identity()
        photos = Photo.query.filter_by(user_id=current_user).all()
        return photos

    @jwt_required
    @api.expect(photo_upload)
    @api.marshal_with(photo_json)
    def post(self):
        """
        Upload a new photo and create thumbnail and processed versions. 
        """
        args = photo_upload.parse_args(request)
        current_user = get_jwt_identity()
        if not args['photo'].filename: 
            abort(401, 'No image selected')
        photo = upload_photo(current_user, args['photo'])
        if not photo:
            abort(401, 'Wrong file type. JPEG/JPG/PNG only!')
        return photo

@ns.route('/thumbnail/<int:photo_id>')
class ThumbnailLink(Resource):
    @jwt_required
    def get(self, photo_id):
        """
        Return the thumbnail photo corresponding to photo_id as a file object 
        """
        photo = Photo.query.get(photo_id)
        path = os.path.join(config['UPLOAD_FOLDER'], photo.thumbnail_link)
        return send_file(path, as_attachment=True)

@ns.route('/original/<int:photo_id>')
class OriginalLink(Resource):
    @jwt_required
    def get(self, photo_id):
        """
        Return the original photo corresponding to photo_id as a file object 
        """
        photo = Photo.query.get(photo_id)
        path = os.path.join(config['UPLOAD_FOLDER'], photo.photo_link)
        return send_file(path, as_attachment=True)

@ns.route('/processed/<int:photo_id>')
class ProcessedLink(Resource):
    @jwt_required
    def get(self, photo_id):
        """
        Return the processed photo corresponding to photo_id as a file object 
        """
        photo = Photo.query.get(photo_id)
        path = os.path.join(config['UPLOAD_FOLDER'], photo.processed_link)
        return send_file(path, as_attachment=True)
        
        



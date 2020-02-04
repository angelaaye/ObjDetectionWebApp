from flask import request, jsonify
from flask_restplus import Resource, reqparse, abort
from api.restplus import api
from flask_jwt_extended import jwt_required

from api.parsers import user_info, photo_upload, photo_info
from api.helpers import upload_photo, process_photo
from api.serializers import photo_json
from database.models import Photo


ns = api.namespace('photo', description='APIs related to ECE1779A1 photo upload/view')


@ns.route('/<int:id>')
class ThumbnailPhotos(Resource):
    @jwt_required
    @api.marshal_with(photo_json)
    def get(self, id):
        """
        Return uploaded photos as thumbnails from access token
        """
        photos = Photo.query.filter_by(user_id=id).all()
        return photos

    @jwt_required
    @api.expect(photo_upload)
    @api.marshal_with(photo_json)
    def post(self, id):
        """
        Upload a new photo
        """
        args = photo_upload.parse_args(request)
        if not args['photo'].filename: 
            abort(401, 'No image selected')
        photo = upload_photo(id, args['photo'])
        if not photo:
            abort(401, 'Wrong file type. JPEG/JPG/PNG only!')
        return photo

@ns.route('/<int:id>/processed')
class ProcessedPhotos(Resource):
    @jwt_required
    @api.expect(photo_info)
    @api.marshal_with(photo_json)
    def get(self, id):
        """
        Return original uploaded photo and the processed photo using OpenCV
        """
        args = photo_info.parse_args(request)
        photo = process_photo(args['photo_id'])
        if not photo:
            abort(401, 'Photo does not exist!')
        return photo
        
        



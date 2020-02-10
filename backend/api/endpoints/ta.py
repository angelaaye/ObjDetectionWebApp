
from flask import request, jsonify
from flask_restplus import Resource, abort
from api.restplus import api
from api.helpers import upload_photo
from api.parsers import photo_upload

from api.parsers import user_info
from api.helpers import create_account, authenticate_user
from api.serializers import user_json


ns = api.namespace('', description='APIs for ECE1779 TA registration and upload photos')

@ns.route('/register')
class Register(Resource):
    @api.expect(user_info)
    @api.marshal_with(user_json)
    def post(self):
        """
        Create a new account and return user
        """
        args = user_info.parse_args(request)
        username = args['username']
        password = args['password']
        if len(username) > 20:
            abort(401, 'Username too long. Please enter a username less than 20 characters.')
        if len(password) > 20:
            abort(401, 'Password too long. Please enter a password less than 20 characters.')
        if len(password) < 4:
            abort(401, 'Password too weak. Please enter a password of at least 4 characters.')
        user = create_account(username=username, password=password)
        if user:
            return user
        else:
            abort(401, 'Username taken')

@ns.route('/upload')
class Upload(Resource):
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
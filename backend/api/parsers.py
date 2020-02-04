from flask_restplus import reqparse
from werkzeug.datastructures import FileStorage

"""
Parsers are 'templates' for information sent as body in POST and PUT requests.
They provide some validation and help swagger generate API documentation.
More info about request parsing: https://flask-restplus.readthedocs.io/en/stable/parsing.html
"""

user_info = reqparse.RequestParser(bundle_errors=True)
user_info.add_argument('username', type=str, required=True, help='Username')
user_info.add_argument('password', type=str, required=True, help='Password')

photo_upload = reqparse.RequestParser(bundle_errors=True)
photo_upload.add_argument('photo', type=FileStorage, location='files', required=True, help='Uploaded photo')

photo_info = reqparse.RequestParser(bundle_errors=True)
photo_info.add_argument('photo_id', type=int, required=True, help='Photo ID')
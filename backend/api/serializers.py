from flask_restplus import fields
from api.restplus import api

"""
Serializers are used to define the structure of the response of endpoints.
The returned object is walked through and serialized using the decorator @api.marshal_with()
More info about response marshaling: https://flask-restplus.readthedocs.io/en/stable/marshalling.html
"""

user_json = api.model('User', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a user'),
    'username': fields.String(description='Username'),
    'password': fields.String(description='Password'),
})

photo_json = api.model('Photo', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a photo'),
    'user_id': fields.Integer(description='User ID'),
    'user': fields.Nested(user_json, description='User object', skip_none=True, allow_null=True),
    'thumbnail_link': fields.String(description='Thumbnail link'),
    'photo_link': fields.String(description='Original photo link'),
    'processed_link': fields.String(description='Processed photo link'),
})
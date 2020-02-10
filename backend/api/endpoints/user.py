from flask import request, jsonify
from flask_restplus import Resource, abort
from api.restplus import api

from api.parsers import user_info
from api.helpers import create_account, authenticate_user
from api.serializers import user_json

from flask_jwt_extended import create_access_token, create_refresh_token, set_access_cookies, \
    set_refresh_cookies, unset_jwt_cookies, get_jwt_identity, jwt_refresh_token_required

import datetime

ns = api.namespace('user', description='APIs related to ECE1779A1 user login/registration')

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
            return user, 200
        else:
            abort(401, 'Username taken.')

@ns.route('/login')
class Login(Resource):
    @api.expect(user_info)
    def post(self):
        """
        Log in a user and returns access and refresh tokens
        """
        args = user_info.parse_args(request)
        username = args['username']
        password = args['password']
        user = authenticate_user(username=username, password=password)
        if user:
            access_token = create_access_token(identity=user.id)
            refresh_token = create_refresh_token(identity=user.id)
            # Set the JWT cookies in the response
            resp = jsonify({
                'login': True
            })
            set_access_cookies(resp, access_token, max_age=86400)
            set_refresh_cookies(resp, refresh_token, max_age=86400)
            return resp
        else:
            abort(401, 'Invalid credentials.')

@ns.route('/logout')
class Logout(Resource):
    def get(self):
        """
        Log out a user
        """
        resp = jsonify({'logout': True})
        unset_jwt_cookies(resp)
        return resp

@ns.route('/refresh-token')
class AuthTokenRefresh(Resource):
    @jwt_refresh_token_required
    def get(self):
        """
        Generate a new access token from a refresh token
        """        
        current_user = get_jwt_identity()
        access_token = create_access_token(identity = current_user)
        # Set the JWT access cookie in the response
        resp = jsonify({
            'refresh': True
        })
        set_access_cookies(resp, access_token, max_age=86400)
        return resp
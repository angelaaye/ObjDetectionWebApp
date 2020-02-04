# Architecture inspired by
# https://github.com/postrational/rest_api_demo/blob/master/rest_api_demo/api/blog/endpoints/posts.py

import os
from flask import Flask, Blueprint
from config import config
from api.endpoints.user import ns as user_namespace
from api.endpoints.photo import ns as photo_namespace
from api.restplus import api
from database import db
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_migrate import Migrate


def create_app():
    # Initialize and configure flask app
    app = Flask(__name__)
    app.config.update(config)
    CORS(app, supports_credentials=True)

    # Initilize database and migrations
    db.init_app(app)
    Migrate(app, db)

    # Register API endpoints (blueprints)
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(user_namespace)
    api.add_namespace(photo_namespace)
    app.register_blueprint(blueprint)

    # Initialize JWT module
    JWTManager(app)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=config['FLASK_DEBUG'], host=config['FLASK_HOST'],
                 port=config['FLASK_PORT'])

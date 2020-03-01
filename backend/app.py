# Architecture inspired by
# https://github.com/postrational/rest_api_demo/blob/master/rest_api_demo/api/blog/endpoints/posts.py

import os
from flask import Flask, Blueprint, send_file
from config import config
from api.endpoints.user import ns as user_namespace
from api.endpoints.photo import ns as photo_namespace
from api.endpoints.ta import ns as ta_namespace
from api.restplus import api
from database import db
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate


def create_app():
    # Initialize and configure flask app
    app = Flask(__name__, static_folder='../frontend/opencv-app/dist/')
    app.config.update(config)

    # Initilize database and migrations
    db.init_app(app)
    Migrate(app, db)

    # Register API endpoints (blueprints)
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(user_namespace)
    api.add_namespace(photo_namespace)
    api.add_namespace(ta_namespace)
    app.register_blueprint(blueprint)

    # Initialize JWT module
    JWTManager(app)

    # Send frontend page
    @app.route('/')
    def index_client():
        entry = os.path.join('../frontend/opencv-app/dist', 'index.html')
        return send_file(entry)

    return app


app = create_app()
app.run(debug=config['FLASK_DEBUG'], host=config['FLASK_HOST'],
             port=config['FLASK_PORT'])

# from dotenv_config import Config
from dotenv import load_dotenv
import os
import json

ENV = 'local' if not 'ENV' in os.environ else os.environ['ENV']

if ENV == 'production':
    load_dotenv('.env.production')
elif ENV == 'development':
    load_dotenv('.env.development')
elif ENV == 'local':
    load_dotenv('.env.local')

config = {}

# Custom settings
config['ENV'] = ENV

# Flask settings
config['FLASK_SERVER_NAME'] = os.getenv('FLASK_SERVER_NAME')
config['FLASK_DEBUG'] = False if ENV == 'production' else True
config['FLASK_ENV'] = 'production' if ENV == 'production' else 'development'
config['FLASK_HOST'] = os.getenv('FLASK_HOST') or '0.0.0.0'
config['FLASK_PORT'] = os.getenv('FLASK_PORT')

# Flask-Restplus settings
config['RESTPLUS_SWAGGER_UI_DOC_EXPANSION'] = os.getenv('RESTPLUS_SWAGGER_UI_DOC_EXPANSION')
config['RESTPLUS_VALIDATE'] = True
config['RESTPLUS_MASK_SWAGGER'] = False
config['RESTPLUS_ERROR_404_HELP'] = False

# JWT settings
# Refer to: https://flask-jwt-extended.readthedocs.io/en/latest/options.html
config['JWT_SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')
config['JWT_TOKEN_LOCATION'] = ['cookies']
# Time in seconds
config['JWT_ACCESS_TOKEN_EXPIRES'] = 86400 

# SQLAlchemy settings
config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')
config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

config['UPLOAD_FOLDER'] = 'uploads'
config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024
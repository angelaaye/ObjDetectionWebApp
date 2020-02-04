import logging
import traceback

from config import config
from flask_restplus import Api
from sqlalchemy.orm.exc import NoResultFound

log = logging.getLogger(__name__)

# Object-like representation of API whose client manifests within Swagger
api = Api(version='1.0', title='ECE1779A1',
          description='OpenCV Web App')


@api.errorhandler
def default_error_handler(e):
    message = 'Server error'
    log.exception(message)

    if not config['FLASK_DEBUG']:
        return {'message': message}, 500


@api.errorhandler(NoResultFound)
def database_not_found_error_handler(e):
    log.warning(traceback.format_exc())
    return {'message': 'A database result was required but none was found.'}, 404
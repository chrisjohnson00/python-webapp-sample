from logging.config import dictConfig
from flask import Flask


def create_app():
    dictConfig({
        'version': 1,
        'formatters': {'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }},
        'handlers': {'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
            'formatter': 'default'
        }},
        'root': {
            'level': 'INFO',
            'handlers': ['wsgi']
        }
    })
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.secret_key = b'8kI*3Z8&8Ce3on@2u2V'

    from . import application

    app.register_blueprint(application.bp)

    return app

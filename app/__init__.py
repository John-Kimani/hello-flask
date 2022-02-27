from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config
import logging

app = Flask(__name__) # flask instance initialization
app.config.from_object(Config) # Inintialize configuration

bootstrap = Bootstrap(app) # Initialize boostrap for flask app
if not app.debug and not app.testing:
    if app.config['LOG_TO_STDOUT']:
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        app.logger.addHandler(stream_handler)
    

from app import routes, errors, models
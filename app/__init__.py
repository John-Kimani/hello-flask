from flask import Flask
from flask_bootstrap import Bootstrap
from config import Config


app = Flask(__name__) # flask instance initialization
app.config.from_object(Config) # Inintialize configuration

bootstrap = Bootstrap(app) # Initialize boostrap for flask app

from app import routes, errors, models
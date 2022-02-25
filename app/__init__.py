from flask import Flask
from flask_bootstrap import Bootstrap


app = Flask(__name__) # flask instance initialization

bootstrap = Bootstrap(app) # Initialize boostrap for flask app

from app import routes, errors, models
import os
from webbrowser import get
class Config(object):
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    NEWS_API_URL = os.environ.get('NEWS_API_URL')
    # NEWS_API_URL = os.environ.get('NEWS_API_URL')
    NEWS_APIKEY = os.environ.get('NEWS_APIKEY')

    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
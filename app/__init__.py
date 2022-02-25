from flask import Flask


app = Flask(__name__) #flask instance initialization


from app import routes, errors, models
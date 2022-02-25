from app import app


@app.route('/')
def index():
    return 'Hello Flask'


@app.route('/')
def about():
    return 'About works'
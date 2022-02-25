from app import app
from flask import render_template
from app.forms import LoginForm, RegistationForm


@app.route('/')
def index():
    return render_template('index.html', title='Home')


@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', title='Log in', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistationForm()
    return render_template('register.html', title='Log in', form=form)
from app import app
from flask import render_template
from app.forms import LoginForm, RegistationForm
from .requests import get_news


@app.route('/')
def index():
    '''
    View root page that retuns index page and data
    '''
    # getting new sources
    news_sources = get_news('general')
    print(news_sources)
    return render_template('index.html', title='Home', news_sources=news_sources)


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
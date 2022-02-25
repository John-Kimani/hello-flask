from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class LoginForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(1, 10)])
    password = PasswordField('password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField()


class RegistationForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(1, 10)])
    email = StringField('Email', validators=[DataRequired(), Length(1,64), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField()
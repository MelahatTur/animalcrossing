from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Regexp

USERNAME_REGEX = r'^[a-zA-Z0-9_.-]{3,20}$'
PASSWORD_REGEX = r'^[a-zA-Z0-9@#$%^&+=]{6,}$'

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(),
        Length(min=3, max=20),
        Regexp(USERNAME_REGEX, message="Invalid username format.")
    ])
    password = PasswordField('Password', validators=[
        DataRequired(),
        Regexp(PASSWORD_REGEX, message="Password must be at least 6 characters.")
    ])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
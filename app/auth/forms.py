from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, Regexp
from wtforms.validators import EqualTo
from wtforms import ValidationError
from ..models import User


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[
        DataRequired(),
        Length(1, 64),
        Email()
    ])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Ricordami')
    submit = SubmitField('Accedi')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[
        DataRequired(),
        Length(1, 64),
        Email()
    ])
    username = StringField('Username',
                           validators=[
                               DataRequired(),
                               Length(1, 64),
                               Regexp('^[A-Za-z][A-Za-z0-9_.]*$',
                                      0,
                                      'Usernames must have only letters, '
                                      'numbers, dots or underscores')])
    password = PasswordField('Password',
                             validators=[
                                 DataRequired(),
                                 EqualTo('password2', message='Le password non coincidono')
                             ])
    password2 = PasswordField('Conferma Password', validators=[DataRequired()])
    submit = SubmitField('Registrati')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email già registrata')

    def validate_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username già in uso')

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Invia')


class EditProfileForm(FlaskForm):
    name = StringField('Nome', validators=[Length(0, 64)])
    location = StringField('Città', validators=[Length(0, 64)])
    about_me = TextAreaField('Biografia')
    submit = SubmitField('Salva')

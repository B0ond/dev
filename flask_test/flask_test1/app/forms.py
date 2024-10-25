# for work need -> poetry add flask_wtf
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms.fields.simple import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, length, EqualTo


class RegistrationForm(FlaskForm):
    name = StringField('ФИО', validators=[DataRequired(), length(min=2, max=100)])
    login = StringField('Логин', validators=[DataRequired(), length(min=2, max=20)])
    password = PasswordField('<PASSWORD>', validators=[DataRequired()])
    confirm_password = PasswordField('<PASSWORD>', validators=[DataRequired(), EqualTo('password')])
    avatar = FileField('Загрузите фото', validators=[FileAllowed(['jpg', 'png', 'jpeg'])])
    submit = SubmitField('Зарегистрироваться')

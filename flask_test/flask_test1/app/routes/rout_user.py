from flask import Blueprint, render_template, redirect, request

from ..functions import save_picture
from ..models.model_user import User
from ..forms import RegistrationForm
from ..extensions import bcrypt, db

user = Blueprint('user', __name__)

@user.route('/user/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
            avatar_filename = save_picture(form.avatar.data)
            user = User(username=form.name.data, login=form.login.data, avatar=avatar_filename, password=hashed_password)
            db.session.add(user)
            db.session.commit()
            print('DEBUG вы зарегистрированы')
            return redirect('/')
        else:
            print('Ошибка регистрации')
    return render_template('user/register.html', form=form)

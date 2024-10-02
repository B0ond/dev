from flask import Blueprint, render_template, redirect

from ..forms import RegistrationForm

user = Blueprint('user', __name__)

@user.route('/user/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        print(form.name.data)
        print(form.password.data)
        print(form.avatar.data)
        return redirect('/')
    else:
        print('Ошибка регистрации')
    return render_template('user/register.html', form=form)

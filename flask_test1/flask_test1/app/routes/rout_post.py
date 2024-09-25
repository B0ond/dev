from flask import Blueprint, render_template, request, redirect
from ..extensions import db
from ..models.model_post import Post

post = Blueprint('post', __name__)

@post.route('/post/create', methods=['POST', 'GET'])
def create():
    if request.method == 'POST':
        teacher = request.form.get('teacher')

        # начало теста
        test = request.form
        url = request.url
        header = request.headers
        args = request.args
        cookies = request.cookies
        print(test)
        print(f'url == {url}')
        print(f'header == {header}')
        print(f'args == {args}')
        print(f'cookies == {cookies}')
        subject = request.form.get('subject')
        student = request.form.get('student')
        # конец теста

        post = Post(teacher=teacher, subject=subject, student=student)
        try:
            db.session.add(post)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            print(str(e))
    else:
        return render_template('post/create.html')

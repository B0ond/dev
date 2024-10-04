import os
import secrets

from flask import current_app  # можем обращаться к конфигурации из разных частей приложения


def save_picture(picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(picture.filename)  #делит картинку на название (_,) и расширение (f_ext)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.config['SERVER_PATH'], picture_fn)
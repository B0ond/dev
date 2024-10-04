import os
import secrets
from tkinter import Image
from PIL import Image

from flask import current_app  # можем обращаться к конфигурации из разных частей приложения


def save_picture(picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(picture.filename)  #делит картинку на название (_,) и расширение (f_ext)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.config['SERVER_PATH'], picture_fn)  # создаем путь дял картинки
    output_size = (125, 125)  # делаем рейсайз картинки
    i = Image.open(picture)  # открываем картинку
    i.thumbnail(output_size)  # обращаемся к картинке
    i.save(picture_path)  # сохраняем по пути
    return picture_fn  # необходимо для бд что бы достать картинку

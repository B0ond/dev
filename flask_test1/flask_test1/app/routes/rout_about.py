from flask import Blueprint, render_template

about = Blueprint('about', __name__)


@about.route('/about')
def index():
    return render_template('about/about.html')

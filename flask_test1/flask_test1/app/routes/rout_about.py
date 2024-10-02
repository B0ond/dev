from flask import Blueprint, render_template

about = Blueprint('about', __name__)


# роут "о нас"
@about.route('/about')
def index():
    return render_template('about/about.html')

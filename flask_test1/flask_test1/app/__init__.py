from flask import Flask, render_template
from dotenv import load_dotenv
from .config import Config

from .extensions import db
import os


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)

    # app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"
    with app.app_context():
        db.create_all()
    load_dotenv()

    bootstrap_css = os.getenv('CSS_BOOTSTRAP')

    @app.context_processor
    def inject_bootstrap_css():
        return dict(bootstrap_css=bootstrap_css)


    @app.route("/")
    def index():
        return render_template('index.html')

    @app.route("/about")
    def about():
        return render_template('about.html')
    return app

if __name__ == "__main__":
    app = create_app()
    app.run()



    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
    # db.init_app(app)
    # with app.app_context():
    #     db.create_all()
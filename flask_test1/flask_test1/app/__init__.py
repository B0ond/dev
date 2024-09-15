import os
from flask import Flask, render_template
from dotenv import load_dotenv
from .config import Config
from .routes.rout_user import user
from .routes.rout_post import post
from .routes.rout_main import main
from .routes.rout_about import about
from .extensions import db, migrate



def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    app.register_blueprint(user)
    app.register_blueprint(post)
    app.register_blueprint(main)
    app.register_blueprint(about)

    db.init_app(app)
    migrate.init_app(app, db)


    # app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"
    with app.app_context():
        db.create_all()

    load_dotenv()
    #bootstrap_css = os.getenv('CSS_BOOTSTRAP')   для работы через env файл

    # @app.context_processor
    # def inject_bootstrap_css():
    #     return dict(bootstrap_css=bootstrap_css)


    # @app.route("/")
    # def index():
    #     return render_template('main/index.html')

    # @app.route("/about")
    # def about():
    #     return render_template('about/about.html')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run()



    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
    # db.init_app(app)
    # with app.app_context():
    #     db.create_all()
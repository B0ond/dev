from flask import Flask, render_template
from dotenv import load_dotenv
from .config import DevConfig
from .routes.rout_user import user
from .routes.rout_post import post
from .routes.rout_about import about
from .extensions import db, migrate


#Главная функция
def create_app(config_class=DevConfig):  # передается класс из config
    app = Flask(__name__)
    app.config.from_object(config_class)
    #регаем блупринты
    app.register_blueprint(user)
    app.register_blueprint(post)
    # app.register_blueprint(main)
    app.register_blueprint(about)

    db.init_app(app)       # работа с бд
    migrate.init_app(app, db)


    # app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"
    with app.app_context():
        db.create_all()

    load_dotenv()  #загрузить переменные из .env
    #bootstrap_css = os.getenv('CSS_BOOTSTRAP')   для работы через env файл

    return app

if __name__ == "__main__":
    app = create_app()
    app.run()


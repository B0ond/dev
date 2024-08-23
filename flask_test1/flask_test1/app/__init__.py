from flask import Flask, render_template
from dotenv import load_dotenv
import os

from sqlalchemy.testing.plugin.bootstrap import bootstrap_file

load_dotenv()


def create_app():
    app = Flask(__name__)

    bootstrap_css = os.getenv('BOOTSTRAP_CSS')


    @app.route("/")
    def index():
        return render_template('index.html', bootstrap_css=bootstrap_css)

    @app.route("/about")
    def about_us():
        return render_template('about.html')
    return app

if __name__ == "__main__":
    app = create_app()
    app.run()
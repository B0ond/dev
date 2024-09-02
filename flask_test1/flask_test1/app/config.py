import os

class Config(object):
    USER = os.environ.get('POSTGRES_USER', 'user')
    PASSWORD = os.environ.get('POSTGRES_PASSWORD', '<PASSWORD>')
    HOST = os.environ.get('POSTGRES_HOST', 'localhost')
    PORT = os.environ.get('POSTGRES_PORT', '5532')
    DB = os.environ.get('POSTGRES_DB', 'mydb')


    SQLALCHEMY_DATABASE_URI = f"postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB}"
    SECRET_KEY = '*&^r64gfisegf7634giwhdfg868^$VEytreuiTY'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

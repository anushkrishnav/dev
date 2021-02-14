import os
from dotenv import load_dotenv

load_dotenv()
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    #its a key used as a signature key used to make sure the content sent isnt intercepted
    SECRET_KEY = os.environ.get('SECRET_KEY') or "secret_string"
    ENV = os.getenv('FLASK_ENV', default='production')
    DEBUG = ENV == 'development'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or  'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = os.environ.get('MAIL_PORT')
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS')
    MAIL_USERNAME = os.environ.get('EMAIL_USER') #set recovery email
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS') #set recovery email password
import os
from dotenv import load_dotenv

load_dotenv()
from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flask_migrate import Migrate
from flask_moment import Moment
from flask_bootstrap import Bootstrap
from flask_pagedown import PageDown
from flask_socketio import SocketIO, emit
from Config import Config

app = Flask(__name__)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
moment = Moment(app)
bootstrap = Bootstrap(app)
pagedown = PageDown(app)
socketio = SocketIO(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config.from_object(Config)
mail = Mail(app)



from dating import routes, models

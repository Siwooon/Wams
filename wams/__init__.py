from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flaskext.markdown import Markdown
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__, static_folder='static')

app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wams.db'
app.config['SECRET_KEY'] = '34d5960ea9a2224236324903'
Markdown(app)
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from wams import routes

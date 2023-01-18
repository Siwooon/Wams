from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flaskext.markdown import Markdown




app = Flask(__name__, static_folder='static')

app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wams.db'
app.config['SECRET_KEY'] = '34d5960ea9a2224236324903'
Markdown(app)
db = SQLAlchemy(app)

from wams import routes

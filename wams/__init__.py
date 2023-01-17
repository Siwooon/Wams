from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///wams.db'
app.config['SECRET_KEY'] = '34d5960ea9a2224236324903'

db = SQLAlchemy(app)

from wams import routes

import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@127.0.0.1/wimsproj'
app.config['SECRET_KEY'] = '75f05e070fc02d9cc742c2e9'
db = SQLAlchemy(app)

from wims import routes
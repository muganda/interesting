from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://interesting:123456@localhost/interesting'
app.testing = True
db = SQLAlchemy(app)

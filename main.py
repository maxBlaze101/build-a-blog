from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://Build-a-Blog:hooyo@localhost:8889/Build-a-Blog"
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
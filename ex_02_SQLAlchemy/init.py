# pip install flask_sqlalchemy
# pip install psycopg2-binary
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import JSON
app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 
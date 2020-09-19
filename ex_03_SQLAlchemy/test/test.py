from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func, distinct
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
import datetime
import json

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:sm1418!1662@192.168.0.13:3306/test'

# SQLALCHEMY_TRACK_MODIFICATIONS : 설명 찾아서 주석달기
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)

class emp(db.Model):
    # __tablename__ = 'emp' #???
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    gender = db.Column(db.String(16))
    age = db.Column(db.String(32))
    location = db.Column(db.Integer)
    deptno = db.Column(db.Integer)
    hiredate = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    salary = db.Column(db.Integer)

results = emp.query.with_entities(emp.location, func.count(emp.id)).group_by(emp.location)
print(results)

for result in results:
    print(result)
from flask import Flask, Response, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func, distinct, case, between
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
import datetime
import json
import pandas as pd


app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:sm1418!1662@192.168.0.13:3306/test'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://scott:tiger@192.168.56.1:3306/test'

# SQLALCHEMY_TRACK_MODIFICATIONS : 옵션을 추가하지 않으면 FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS 경고메시지 발생
# ['SQLALCHEMY_TRACK_MODIFICATIONS'] = True -> sqlalchemy가 객체 수정을 추적하고 신호를 보냄 (추가적인 메모리를 사용)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)
CORS(app)

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

if __name__ == '__main__':
    # results = db.session.query(emp).with_entities(emp.location, func.count(emp.id)).group_by(emp.location)
    results = db.session.query(emp).with_entities(
        func.avg(
            case(
                [
                    (emp.age <30, emp.salary)
                ]
                # ,else_='null'
            )
         ).label('30대 이하 연봉 평균'),
        func.avg(
            case(
                [
                    (between(emp.age, 30, 39), emp.salary)
                ]
            )
         ).label('30대 연봉 평균'),
        func.avg(
            case(
                [
                    (between(emp.age, 40, 49), emp.salary)
                ]
            )
         ).label('40대 연봉 평균'),
        func.avg(
            case(
                [
                    (emp.age >=50, emp.salary)
                ]
            )
         ).label('50대 이상 연봉 평균')    
    )
    print(results)
    for result in results:
        print(result)
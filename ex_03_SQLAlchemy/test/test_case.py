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
def makeJsonWithCaseOption(orm_result, caseOption):
    exceptionCase = ['06_02', '06_03', '06_04']
    if caseOption not in exceptionCase:
        return ormConvertToJson(orm_result)
    else: # .all(), .first(), .scalar()
        return orm_result

# orm의 결과를 받아서 json형태로 바꿔주는 함수
# .all(), .first(), .scalar()등의 함수를 사용할 경우 orm_result.statement부분이 사라져 사용할 수 없음
def ormConvertToJson(orm_result):
    df = pd.read_sql(orm_result.statement, orm_result.session.bind)

    #orient='index'(json format의 default값) -> dict like {index -> {column->value}}
    #orient='records' -> list like [{column -> value}, ... ]
    result = json.loads(df.to_json(orient='records'))
    return result

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
                    #between은 왼쪽 오른쪽 값들을 다 포함함(target, left, right)
                    #정확히 left, right값일 경우에도 true로 판별(초과, 미만이아닌 이상, 이하로..)
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
    result = ormConvertToJson(results)
    print(result)
from flask import Flask, Response
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
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
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    gender = db.Column(db.String(16))
    age = db.Column(db.String(32))
    location = db.Column(db.Integer)
    deptno = db.Column(db.Integer)
    hiredate = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    salary = db.Column(db.Integer)

# orm의 결과를 받아서 json형태로 바꿔주는 함수
# .all(), .first(), .sclar()등의 함수를 사용할 경우 orm_result.statement부분이 사라져 사용할 수 없음
def ormConvertToJson(orm_result):
    df = pd.read_sql(orm_result.statement, orm_result.session.bind)

    #orient='index'(json format의 default값) -> dict like {index -> {column->value}}
    #orient='records' -> list like [{column -> value}, ... ]
    result = json.loads(df.to_json(orient='records'))
    return result

@app.route('/test')
def test():
    result = {'key':'value'}

    return Response(
        response = json.dumps(result),
        status = 200,
        mimetype="application/json"
    )

@app.route('/check_orm')
def check_orm():    
    results = emp.query.with_entities(emp.location, func.count(emp.id).label('count')).group_by(emp.location)

    # ORM에서 변환된 SQL문을 콘솔로 확인
    print(results)

    result = ormConvertToJson(results)

    return Response(
        response = json.dumps(result),
        status = 200,
        mimetype="application/json"
    )

if __name__ == '__main__':
    # app.run(host="192.168.0.51", port="5000")
    app.run(host="192.168.56.1", port="5000")



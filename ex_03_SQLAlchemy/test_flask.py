from flask import Flask, Response
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
import datetime
import json
import pandas as pd


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

@app.route('/test_response')
def test_response():
    result = {'key1':'value1', 'key2':'value2'}
    return Response(
        response = json.dumps(result),
        status = 200,
        mimetype="application/json"
    )

@app.route('/check_orm')
def check_orm():    
    # results = emp.query.with_entities(func.count(emp.id).label('count'), func.avg(emp.salary).label('salary_average'), emp.location.label('location'), (func.floor((emp.age)/10)*10).label('연령대별')).group_by(emp.location, func.floor((emp.age)/10))
    # results = emp.query.filter(emp.gender=='m').with_entities(emp.location, func.count(emp.id)).group_by(emp.location).having(func.count(emp.id)>1).order_by(func.count(emp.id).desc())
    results = emp.query.with_entities(emp.location, func.count(emp.id).label('count')).group_by(emp.location)

    # ORM에서 변환된 SQL문을 콘솔로 확인
    print(results)

    #query 결과를 json형태로 변환
    df = pd.read_sql(results.statement, results.session.bind)
    
    #orient='index'(json format의 default값) -> dict like {index -> {column->value}}
    #orient='records' -> list like [{column -> value}, ... ]
    result = json.loads(df.to_json(orient='records'))

    return Response(
        response = json.dumps(result),
        status = 200,
        mimetype="application/json"
    )

if __name__ == '__main__':
    app.run(host="192.168.0.51", port="5000")



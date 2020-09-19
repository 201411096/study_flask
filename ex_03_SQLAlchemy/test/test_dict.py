from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
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

if __name__ == '__main__':
    results = emp.query.with_entities(func.count(emp.id).label('count'), func.avg(emp.salary).label('salary_average'), emp.location.label('location'), (func.floor((emp.age)/10)*10).label('연령대별')).group_by(emp.location, func.floor((emp.age)/10))
    json_result = {}
    # for result in results:
    #     json_result[result[2]+str(result[3])] = {
    #         'avg_sal' : result[1],
    #         'count' : result[0]
    #     }
    # print(json_result['busan30'])
    for result in results:
            json_result[str(result[3])] = {result[2]:
                {
                    'avg_sal' : result[1],
                    'count' : result[0]
                }
            }
    print(json_result)
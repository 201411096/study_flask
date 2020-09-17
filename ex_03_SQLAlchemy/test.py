from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:sm1418!1662@192.168.0.13:3306/test'

db = SQLAlchemy(app)

class emp(db.Model):
    __tablename__ = 'emp'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    gender = db.Column(db.String(16))
    age = db.Column(db.String(32))
    location = db.Column(db.Integer)
    deptno = db.Column(db.Integer)
    hiredate = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    salary = db.Column(db.Integer)

if __name__ == '__main__':
    # case_01_단순 group query
    # results = emp.query.with_entities(emp.location, func.count(emp.id)).group_by(emp.location)
    # case_02_group by having
    # results = emp.query.with_entities(emp.location, func.count(emp.id)).group_by(emp.location).having(func.count(emp.id)>1)
    # case_03_group by having order by
    # results = emp.query.with_entities(emp.location, func.count(emp.id)).group_by(emp.location).having(func.count(emp.id)>1).order_by(func.count(emp.id).desc())
    # case_04_group by where having order by
    # ** .filter와 .with_entities의 순서가 의미없는듯 **
    # results = emp.query.filter(emp.gender=='m').with_entities(emp.location, func.count(emp.id)).group_by(emp.location).having(func.count(emp.id)>1).order_by(func.count(emp.id).desc())
    # results = emp.query.with_entities(emp.location, func.count(emp.id)).filter(emp.gender=='w').group_by(emp.location).having(func.count(emp.id)>1).order_by(func.count(emp.id).desc())
    # case_05_01 다중 컬럼 group query    
    # results = emp.query.with_entities(func.count(emp.id), emp.location, emp.deptno).group_by(emp.location, emp.deptno)
    # case_05_02 다중 컬럼 group query
    # results = emp.query.with_entities(func.count(emp.id), emp.location, func.floor((emp.age)/10).label('연령대별')).group_by(emp.location, func.floor((emp.age)/10))
    # results = emp.query.with_entities(func.count(emp.id).label('count'), func.avg(emp.salary).label('salary_average'), emp.location, (func.floor((emp.age)/10)*10).label('연령대별')).group_by(emp.location, func.floor((emp.age)/10))
    # case_06 subquery (평균 대비 편차구하기)
    # avg_age = emp.query.with_entities(func.avg(emp.age).label('age')).first()
    # results = emp.query.with_entities((emp.age-avg_age).label('평균나이 별 편차'), emp.age, emp.id)
    # case_07_01 추가적인예시(특정 조건의 전체자료 가져오기 )
    # results = emp.query.filter(emp.gender=='m').all()    
    # case_07_02 추가적인예시(특정 조건의 첫번쨰자료 가져오기 )
    # results = emp.query.filter(emp.gender=='m').first()    
    # print(results)
    # case_07_03 scalar()를 활용한 조건 검색
    # try:
    #     results = emp.query.filter(emp.gender=='m').scalar()    
    #     print(results)
    # except NoResultFound:
    #     print('결과값이 존재하지 않습니다.')
    # except MultipleResultsFound:
    #     print('두개 이상의 결과가 발견되었습니다.')
    for result in results:
        print(result)
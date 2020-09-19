from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func, distinct
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
import datetime
import json
import pandas as pd

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:sm1418!1662@192.168.0.13:3306/test'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://scott:tiger@192.168.56.1:3306/test'

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

# orm의 결과를 받아서 json형태로 바꿔주는 함수
# .all(), .first(), .sclar()등의 함수를 사용할 경우 orm_result.statement부분이 사라져 사용할 수 없음
def ormConvertToJson(orm_result):
    df = pd.read_sql(orm_result.statement, orm_result.session.bind)
    result = json.loads(df.to_json(orient='records'))
    return result

if __name__ == '__main__':
    # case_01_01_단순 group query
    # results = db.session.query(emp).with_entities(emp.location, func.count(emp.id)).group_by(emp.location)
    # case_01_02_group query with distinct count
    # results = db.session.query(emp).with_entities(emp.gender, func.count(distinct(emp.location)), func.count(emp.id)).group_by(emp.gender)
    # case_02_group by having
    # results = db.session.query(emp).with_entities(emp.location, func.count(emp.id)).group_by(emp.location).having(func.count(emp.id)>1)
    # case_03_group by having order by
    # results = db.session.query(emp).with_entities(emp.location, func.count(emp.id)).group_by(emp.location).having(func.count(emp.id)>1).order_by(func.count(emp.id).desc())
    # case_04_group by where having order by
    # results = db.session.query(emp).filter(emp.gender=='m').with_entities(emp.location, func.count(emp.id)).group_by(emp.location).having(func.count(emp.id)>1).order_by(func.count(emp.id).desc())
    # case_05_01 다중 컬럼 group query    
    # results = db.session.query(emp).with_entities(func.count(emp.id), emp.location, emp.deptno).group_by(emp.location, emp.deptno)
    # case_05_02 다중 컬럼 group query
    # results = db.session.query(emp).with_entities(func.count(emp.id).label('count'), func.avg(emp.salary).label('salary_average'), emp.location.label('location'), (func.floor((emp.age)/10)*10).label('연령대별')).group_by(emp.location, func.floor((emp.age)/10))
    # case_06_01 추가적인예시(평균 대비 편차구하기)
    # avg_age = db.session.query(emp).with_entities(func.avg(emp.age).label('age')).first()
    # results = db.session.query(emp).with_entities((emp.age-avg_age).label('평균나이 별 편차'), emp.age, emp.id)
    # case_06_02 추가적인예시(특정 조건의 전체자료 가져오기 )
    # results = db.session.query(emp).filter(emp.gender=='m').all()   
    # case_06_03 추가적인예시(특정 조건의 첫번째자료 가져오기 )
    # results =db.session.query(emp).filter(emp.gender=='m').first()
    # print(results)
    # case_06_04 scalar()를 활용한 조건 검색
    # try:
    #     results = db.session.query(emp).filter(emp.name=='aaa').scalar()    
    #     print(results)
    # except NoResultFound:
    #     print('결과값이 존재하지 않습니다.')
    # except MultipleResultsFound:
    #     print('두개 이상의 결과가 발견되었습니다.')
    # case_06_05 추가적인예시(연령대(30대미만,30, 40, 50대 이상)별 평균연봉)
    # tmp1 = db.session.query(emp).with_entities(func.avg(emp.salary).label('avg_sal')).filter(emp.age<30).one()
    # tmp2 = db.session.query(emp).with_entities(func.avg(emp.salary).label('avg_sal')).filter(emp.age>=30).filter(emp.age<40).one()
    # tmp3 = db.session.query(emp).with_entities(func.avg(emp.salary).label('avg_sal')).filter(emp.age>=40).filter(emp.age<50).one()
    # tmp4 = db.session.query(emp).with_entities(func.avg(emp.salary).label('avg_sal')).filter(emp.age>=50).one()
    # results = {'30대미만 평균연봉': tmp1.avg_sal, '30대 평균연봉':tmp2.avg_sal, '40대 평균연봉':tmp3.avg_sal, '50대이상 평균연봉':tmp4.avg_sal}
    # print(results)
    # print(results['30대 평균연봉'])
    # case_06_06 추가적인예시(전체나이 합계에 차지하는 개별나이의 비율)
    # tmp1 = db.session.query(emp).with_entities(func.count(emp.id).label('countid'), emp.age.label('age')).group_by(emp.age)
    # results = db.session.query(emp).with_entities(emp.location, func.count(emp.id)).group_by(emp.location)

    subq1 = db.session.query(emp).with_entities(func.count(emp.id).label('countid'), emp.age.label('age')).group_by(emp.age).subquery()
    subq2 = db.session.query(emp).with_entities(func.sum(emp.age).label('agesum')).subquery()
    results = db.session.query(subq1, subq2).with_entities(subq1.c.age, (subq1.c.age*subq1.c.countid/subq2.c.agesum*100).label('rate'))
    print(results)

    #1
    # result = ormConvertToJson(results)
    # print(result)

    #2
    for result in results:
        print(result)

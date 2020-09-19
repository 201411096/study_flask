from flask import Flask, Response, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func, distinct
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

def makeJsonWithCaseOption(orm_result, caseOption):
    exceptionCase = ['06_02', '06_03', '06_04', '06_05']
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

def checkQueryInConsole(orm_result, caseOption):
    print('-------------------------------------------------------------')
    print('Query : ' + caseOption)
    print(orm_result)
    print('-------------------------------------------------------------')

@app.route('/test')
def test():
    result = {'key':'value'}

    return Response(
        response = json.dumps(result),
        status = 200,
        mimetype="application/json"
    )

def testCase(case):
    results = {}
    # case_01_01_단순 group query
    # select count(id) from emp group by location
    if case=='01_01':
        results = db.session.query(emp).with_entities(emp.location, func.count(emp.id)).group_by(emp.location)
    # case_01_02_group query with distinct count
    # SELECT gender, COUNT(gender), COUNT(DISTINCT location) FROM emp GROUP BY gender
    elif case=='01_02':
        results = db.session.query(emp).with_entities(emp.gender, func.count(distinct(emp.location)), func.count(emp.id)).group_by(emp.gender)
    # case_02_having절을 포함한 group query
    # select count(id), location from emp group by location HAVING COUNT(id)>2;
    elif case=='02':
        results = db.session.query(emp).with_entities(emp.location, func.count(emp.id)).group_by(emp.location).having(func.count(emp.id)>1)
    # case_03_order by절을 포함한 group query
    # select count(id), location from emp group by location HAVING COUNT(id)>1 ORDER BY COUNT(id) desc;
    elif case=='03':
        results = db.session.query(emp).with_entities(emp.location, func.count(emp.id)).group_by(emp.location).having(func.count(emp.id)>1).order_by(func.count(emp.id).desc())
    # case_04 where절을 포함한 group query
    # select count(id), location from emp WHERE gender = 'm' group by location HAVING COUNT(id)>1 ORDER BY COUNT(id) desc;
    elif case=='04':
        results = db.session.query(emp).filter(emp.gender=='m').with_entities(emp.location, func.count(emp.id)).group_by(emp.location).having(func.count(emp.id)>1).order_by(func.count(emp.id).desc())
    # case_05_01 다중 컬럼 group query
    # SELECT COUNT(id), location, deptno FROM emp GROUP BY location, deptno;
    elif case=='05_01':
        results = db.session.query(emp).with_entities(func.count(emp.id), emp.location, emp.deptno).group_by(emp.location, emp.deptno)
    # case_05_02 다중 컬럼 group query(지역, 연령별 평균연봉)
    # SELECT location,concat(FLOOR(age/10), '0대' ) AS '연령대', AVG(salary) AS 'salary_average', count(id) FROM emp GROUP BY location, FLOOR(age/10);
    elif case=='05_02':
        results = db.session.query(emp).with_entities(func.count(emp.id).label('count'), func.avg(emp.salary).label('salary_average'), emp.location.label('location'), (func.floor((emp.age)/10)*10).label('연령대별')).group_by(emp.location, func.floor((emp.age)/10))
    # case_06_01 추가적인예시(평균 대비 편차구하기)
    # SELECT e.age-a.avg_age FROM emp e, (SELECT AVG(age) AS avg_age FROM emp) a
    elif case=='06_01':
        avg_age = db.session.query(emp).with_entities(func.avg(emp.age).label('age')).first()
        results = db.session.query(emp).with_entities((emp.age-avg_age).label('평균나이 별 편차'), emp.age, emp.id)
    # case_06_02 추가적인예시(특정 조건의 전체자료 가져오기 )
    # SELECT id, name FROM emp WHERE gender='m'
    elif case=='06_02':
        results = db.session.query(emp).filter(emp.gender=='m').with_entities(emp.id, emp.name).all()   
    # case_06_03 추가적인예시(특정 조건의 첫번쨰자료 가져오기 )
    # SELECT id, name FROM emp WHERE gender='m' LIMIT 1
    elif case=='06_03':
        results =db.session.query(emp).filter(emp.gender=='m').with_entities(emp.id, emp.name).first()
    # case_06_04 scalar()를 활용한 조건검색(한가지 값을 검색하며 검색결과가 없거나 두개 이상일 경우 예외처리)
    # SELECT id, name FROM emp WHERE gender='m' LIMIT 1
    elif case=='06_04':
        try:
            results = db.session.query(emp).filter(emp.name=='aaa').with_entities(emp.id, emp.name).scalar()    
            print(results)
        except NoResultFound:
            print('결과값이 존재하지 않습니다.')
        except MultipleResultsFound:
            print('두개 이상의 결과가 발견되었습니다.')
    # case_06_05 추가적인예시(연령대(30대미만, 30대, 40대, 50대이상)별 평균연봉)
    # SELECT tmp1.avg_sal AS '30대미만 평균연봉', tmp2.avg_sal AS '30대 평균연봉', tmp3.avg_sal AS '40대 평균연봉', tmp4.avg_sal AS '50대이상 평균연봉' FROM 
    # (SELECT AVG(salary) AS avg_sal FROM emp WHERE age < 30) tmp1,
    # (SELECT AVG(salary) AS avg_sal FROM emp WHERE age >=30 AND age <40) tmp2,
    # (SELECT AVG(salary) AS avg_sal FROM emp WHERE age >=40 AND age <50) tmp3,
    # (SELECT AVG(salary) AS avg_sal FROM emp WHERE age >= 50) tmp4    
    elif case=='06_05':
        tmp1 = db.session.query(emp).with_entities(func.avg(emp.salary).label('avg_sal')).filter(emp.age<30).one()
        tmp2 = db.session.query(emp).with_entities(func.avg(emp.salary).label('avg_sal')).filter(emp.age>=30).filter(emp.age<40).one()
        tmp3 = db.session.query(emp).with_entities(func.avg(emp.salary).label('avg_sal')).filter(emp.age>=40).filter(emp.age<50).one()
        tmp4 = db.session.query(emp).with_entities(func.avg(emp.salary).label('avg_sal')).filter(emp.age>=50).one()
        results = {'30대미만 평균연봉': tmp1.avg_sal, '30대 평균연봉':tmp2.avg_sal, '40대 평균연봉':tmp3.avg_sal, '50대이상 평균연봉':tmp4.avg_sal}
    # case_06_06 추가적인예시(전체나이 합계에 차지하는 개별나이의 비율) - subquery
	# SELECT a.age AS age, a.age*a.countid/b.agesum*100 as rate FROM
	# (SELECT COUNT(id) AS countid, age FROM emp GROUP BY age) a,
	# (SELECT SUM(age) AS agesum FROM emp) b;    
    elif case=='06_06':
        subq1 = db.session.query(emp).with_entities(func.count(emp.id).label('countid'), emp.age.label('age')).group_by(emp.age).subquery()
        subq2 = db.session.query(emp).with_entities(func.sum(emp.age).label('agesum')).subquery()
        results = db.session.query(subq1, subq2).with_entities(subq1.c.age, (subq1.c.age*subq1.c.countid/subq2.c.agesum*100).label('rate'))
    
    return results

@app.route('/test_orm')
def test_orm():    
    caseOption = request.args.get('case')
    results = testCase(caseOption)
    # ORM에서 변환된 SQL문을 콘솔로 확인
    checkQueryInConsole(results, caseOption)

    result = makeJsonWithCaseOption(results, caseOption)

    return Response(
        response = json.dumps(result),
        status = 200,
        mimetype="application/json"
    )

if __name__ == '__main__':
    # app.run(host="192.168.0.51", port="5000")
    app.run(host="192.168.56.1", port="5000")



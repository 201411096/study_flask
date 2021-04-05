from flask import Flask, Response, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func, distinct, case, between
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
import datetime
import json
import pandas as pd
from sqlalchemy.dialects.mysql import \
        BIGINT, BINARY, BIT, BLOB, BOOLEAN, CHAR, DATE, \
        DATETIME, DECIMAL, DECIMAL, DOUBLE, ENUM, FLOAT, INTEGER, \
        LONGBLOB, LONGTEXT, MEDIUMBLOB, MEDIUMINT, MEDIUMTEXT, NCHAR, \
        NUMERIC, NVARCHAR, REAL, SET, SMALLINT, TEXT, TIME, TIMESTAMP, \
        TINYBLOB, TINYINT, TINYTEXT, VARBINARY, VARCHAR, YEAR


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:sm1418!1662@192.168.0.13:3306/test'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://scott:tiger@192.168.56.1:3306/test'

# SQLALCHEMY_TRACK_MODIFICATIONS : 옵션을 추가하지 않으면 FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS 경고메시지 발생
# ['SQLALCHEMY_TRACK_MODIFICATIONS'] = True -> sqlalchemy가 객체 수정을 추적하고 신호를 보냄 (추가적인 메모리를 사용)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)
CORS(app)

# 샘플데이터1 구조
class emp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    gender = db.Column(db.String(16))
    age = db.Column(db.Integer)
    location = db.Column(db.Integer)
    deptno = db.Column(db.Integer)
    hiredate = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    salary = db.Column(db.Integer)

# 샘플데이터2 구조
class board(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    writer_id = db.Column(db.String(64))
    title = db.Column(db.String(128))
    content = db.Column(LONGTEXT)

def makeJsonWithCaseOption(orm_result):
    try:
        return ormConvertToJson(orm_result)
    # .scalar(), .all(), .first(), .one()함수를 사용할 경우 .statement attribute가 존재하지 않아 attributeError가 발생함
    except AttributeError:
        return json.dumps(orm_result)

# orm의 결과를 받아서 json형태로 바꿔주는 함수
# .all(), .first(), .scalar()등의 함수를 사용할 경우 orm_result.statement부분이 사라져 사용할 수 없음
def ormConvertToJson(orm_result):
    df = pd.read_sql(orm_result.statement, orm_result.session.bind)

    #orient='index'(json format의 default값) -> dict like {index -> {column->value}}
    #orient='records' -> list like [{column -> value}, ... ]
    result = df.to_json(orient='records')

    return result

# orm에서 변환된 쿼리문을 콘솔에서 확인
def checkQueryInConsole(orm_result, caseOption):
    print('-------------------------------------------------------------')
    print('Query : ' + caseOption)
    print(orm_result)
    print('-------------------------------------------------------------')

# 테스트
@app.route('/test')
def test():
    result = {'key':'value'}

    return Response(
        response = json.dumps(result),
        status = 200,
        mimetype="application/json"
    )

# caseOption에 해당하는 쿼리결과를 반환
def testCase(caseOption):
    results = {}

    # case_01_01_단순 group query
    # select count(id) from emp group by location
    if caseOption=='01_01':
        results = db.session.query(emp)\
            .with_entities(
                emp.location, 
                func.count(emp.id),
                func.count(emp.id).label('count') # label 사용 이유
            ).group_by(emp.location)
        
    # case_01_02_group query with distinct count
    # SELECT gender, COUNT(gender), COUNT(DISTINCT location) FROM emp GROUP BY gender
    elif caseOption=='01_02':
        results = db.session.query(emp)\
            .with_entities(
                emp.gender, 
                func.count(distinct(emp.location)), 
                func.count(emp.id)
            ).group_by(emp.gender)

    # case_02_having절을 포함한 group query
    # select count(id), location from emp group by location HAVING COUNT(id)>2;
    elif caseOption=='02':
        results = db.session.query(emp)\
            .with_entities(
                emp.location, 
                func.count(emp.id)
            ).group_by(emp.location)\
            .having(func.count(emp.id)>1)

    # case_03_order by절을 포함한 group query
    # select count(id), location from emp group by location HAVING COUNT(id)>1 ORDER BY COUNT(id) desc;
    elif caseOption=='03':
        results = db.session.query(emp)\
            .with_entities(
                emp.location, 
                func.count(emp.id)
            ).group_by(emp.location)\
            .having(func.count(emp.id)>1)\
            .order_by(func.count(emp.id).desc())

    # case_04 where절을 포함한 group query
    # select count(id), location from emp WHERE gender = 'm' group by location HAVING COUNT(id)>1 ORDER BY COUNT(id) desc;
    elif caseOption=='04':
        results = db.session.query(emp)\
            .filter(emp.gender=='m')\
            .with_entities(
                emp.location, 
                func.count(emp.id)
            ).group_by(emp.location)\
            .having(func.count(emp.id)>1)\
            .order_by(func.count(emp.id).desc())

    # case_05_01 다중 컬럼 group query
    # SELECT COUNT(id), location, deptno FROM emp GROUP BY location, deptno;
    elif caseOption=='05_01':
        results = db.session.query(emp)\
            .with_entities(
                func.count(emp.id), 
                emp.location, 
                emp.deptno
            ).group_by(emp.location, emp.deptno)

    # case_05_02 다중 컬럼 group query(지역, 연령별 평균연봉)
    # SELECT location,concat(FLOOR(age/10), '0대' ) AS '연령대', AVG(salary) AS 'salary_average', count(id) FROM emp GROUP BY location, FLOOR(age/10);
    elif caseOption=='05_02':
        results = db.session.query(emp)\
            .with_entities(
                func.count(emp.id).label('count'), 
                func.avg(emp.salary).label('salary_average'), 
                emp.location.label('location'), 
                (func.floor((emp.age)/10)*10).label('연령대별')
                ).group_by(
                    emp.location, 
                    func.floor((emp.age)/10))

    # case_06_01 추가적인예시(평균 대비 편차구하기)
    # SELECT e.age-a.avg_age FROM emp e, (SELECT AVG(age) AS avg_age FROM emp) a
    elif caseOption=='06_01':
        avg_age = db.session.query(emp)\
            .with_entities(
                func.avg(emp.age).label('age')
            ).subquery()
        results = db.session.query(emp, avg_age)\
            .with_entities(
                emp.id, 
                emp.name, 
                emp.age, 
                avg_age.c.age.label('평균나이'), 
                (emp.age-avg_age.c.age).label('평균나이 별 편차')
            )

    # case_06_02 추가적인예시(특정 조건의 전체자료 가져오기 )
    # SELECT id, name FROM emp WHERE gender='m'
    elif caseOption=='06_02':
        # results = db.session.query(emp).filter(emp.gender=='m').with_entities(emp.id, emp.name).all()   
        results = db.session.query(emp)\
            .filter(emp.gender=='m')\
            .with_entities(
                emp.id.label('id'), 
                emp.name.label('name')
            ).all()   

    # case_06_03 추가적인예시(특정 조건의 첫번쨰자료 가져오기 )
    # SELECT id, name FROM emp WHERE gender='m' LIMIT 1
    elif caseOption=='06_03':
        results =db.session.query(emp)\
            .filter(emp.gender=='m')\
                .with_entities(
                    emp.id, 
                    emp.name
                ).first()

    # case_06_04 scalar()를 활용한 조건검색(한가지 값을 검색하며 검색결과가 없거나 두개 이상일 경우 예외처리)
    # SELECT id, name FROM emp WHERE gender='m' LIMIT 1
    elif caseOption=='06_04':
        try:
            results = db.session.query(emp)\
                .filter(emp.name=='aaa')\
                    .with_entities(
                        emp.id, 
                        emp.name
                    ).scalar()    
            print(results)
        except NoResultFound:
            print('결과값이 존재하지 않습니다.')
        except MultipleResultsFound:
            print('두개 이상의 결과가 발견되었습니다.')

    # case_06_05 추가적인예시(연령대(30대미만, 30대, 40대, 50대이상)별 평균연봉)
    # case-when을 사용하기 전 query
    # SELECT tmp1.avg_sal AS '30대미만 평균연봉', tmp2.avg_sal AS '30대 평균연봉', tmp3.avg_sal AS '40대 평균연봉', tmp4.avg_sal AS '50대이상 평균연봉' FROM 
    # (SELECT AVG(salary) AS avg_sal FROM emp WHERE age < 30) tmp1,
    # (SELECT AVG(salary) AS avg_sal FROM emp WHERE age >=30 AND age <40) tmp2,
    # (SELECT AVG(salary) AS avg_sal FROM emp WHERE age >=40 AND age <50) tmp3,
    # (SELECT AVG(salary) AS avg_sal FROM emp WHERE age >= 50) tmp4    
    elif caseOption=='06_05':
        tmp1 = db.session.query(emp).with_entities(func.avg(emp.salary).label('avg_sal')).filter(emp.age<30).subquery()
        tmp2 = db.session.query(emp).with_entities(func.avg(emp.salary).label('avg_sal')).filter(emp.age>=30).filter(emp.age<40).subquery()
        tmp3 = db.session.query(emp).with_entities(func.avg(emp.salary).label('avg_sal')).filter(emp.age>=40).filter(emp.age<50).subquery()
        tmp4 = db.session.query(emp).with_entities(func.avg(emp.salary).label('avg_sal')).filter(emp.age>=50).subquery()
        results = db.session.query(tmp1, tmp2, tmp3, tmp4)\
            .with_entities(
                tmp1.c.avg_sal.label('30대 미만 연봉'), 
                tmp2.c.avg_sal.label('30대 연봉'), 
                tmp3.c.avg_sal.label('40대 연봉'), 
                tmp4.c.avg_sal.label('50대 이상 연봉'))

    # case_06_05_02 추가적인예시(연령대(30대미만, 30대, 40대, 50대이상)별 평균연봉) - case-when 사용
    # select 
    # avg(case when age<30 then salary end) as '30대 미만 연봉',
    # avg(case when (age>=30 and age<40) then salary end) as '30대 연봉',
    # avg(case when (age>=40 and age<50) then salary end) as '40대 연봉',
    # avg(case when age>=50 then salary end) as '50대 이상 연봉'
    # from emp;
    elif caseOption=='06_05_02':
        print('check in case 06_05_02 ...')
        results = db.session.query(emp).with_entities(
            emp.location,
            func.ifnull(
                func.avg(
                    case(
                        [
                            (emp.age <30, emp.salary)
                        ]
                    )
                ), 0
            )
            .label('30대 이하 연봉 평균'),
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
        ).group_by(emp.location)

    # case_06_06 추가적인예시(전체나이 합계에 차지하는 개별나이의 비율) - subquery
	# SELECT a.age AS age, a.age*a.countid/b.agesum*100 as rate FROM
	# (SELECT COUNT(id) AS countid, age FROM emp GROUP BY age) a,
	# (SELECT SUM(age) AS agesum FROM emp) b;    
    elif caseOption=='06_06':
        subq1 = db.session.query(emp)\
            .with_entities(
                func.count(emp.id).label('countid'), 
                emp.age.label('age')
            ).group_by(emp.age).subquery()
        subq2 = db.session.query(emp)\
            .with_entities(func.sum(emp.age).label('agesum')).subquery()
        results = db.session.query(subq1, subq2)\
            .with_entities(
                subq1.c.age, 
                subq1.c.countid.label('count'), 
                (subq1.c.age*subq1.c.countid).label('age * count'), 
                subq2.c.agesum, (subq1.c.age*subq1.c.countid/subq2.c.agesum*100).label('rate'))
    
    # case_07_01 null검색
    # select * from board where content is null;
    elif caseOption=='07_01':
        results = db.session.query(board)\
            .with_entities(
                board.id, 
                board.writer_id, 
                board.title, 
                board.content
            ).filter(board.content == None)

    # case_07_02_01 '' 검색
    # select * from board where content is '';
    elif caseOption=='07_02_01':
        results = db.session.query(board)\
            .with_entities(
                board.id, 
                board.writer_id, 
                board.title, 
                board.content
            ).filter(board.content == '')
    
    # case_07_02_02 ' ' 검색
    # select * from board where content is ' ';
    elif caseOption=='07_02_02':
        results = db.session.query(board)\
            .with_entities(
                board.id, 
                board.writer_id, 
                board.title, 
                board.content
            ).filter(board.content == ' ')

    # case_07_03 ifnull()
    # select id, writer_id, title, ifnull(content, 'default_board_content') as content from board where content is null;
    elif caseOption=='07_03':
        results = db.session.query(board)\
            .with_entities(
                board.id, 
                board.writer_id, 
                board.title, 
                func.ifnull(board.content, 'default_board_content').label('content')
            ).filter(board.content == None)

    # case_07_04 between()
    # select * from board where id >=5 and id<=10;
    elif caseOption=='07_04':
        results = db.session.query(board)\
            .with_entities(
                board.id, 
                board.writer_id, 
                board.title, 
                board.content
            ).filter(between(board.id, 5, 10))

    # case_07_05 like()
    # select * from board where content like '%aaa%';
    elif caseOption=='07_05':
        results = db.session.query(board)\
            .with_entities(
                board.id, 
                board.writer_id, 
                board.title, 
                board.content
            ).filter(board.content.like("%aaa%"))

    return results

@app.route('/test_raw_sql')
def test_raw_sql():
    arg_sql_query = request.args.get('query')

    checkQueryInConsole(arg_sql_query, 'raw_sql') # querystring으로 넘겨받은 sql문을 콘솔에서 확인

    results = db.session.execute(arg_sql_query) # sql를 실행결과를 받음(resultProxy형태)

    # resultProxy -> dict
    result = []
    for row in results:
        result.append(dict(row))

    return Response(
        response = json.dumps(result), # dict -> json
        status = 200,
        mimetype="application/json"
    )

# test 예시
# http://192.168.56.1:5000/test_orm?case=07_01
@app.route('/test_orm')
def test_orm():    
    caseOption = request.args.get('case')
    results = testCase(caseOption)

    # ORM에서 변환된 SQL문을 콘솔로 확인
    checkQueryInConsole(results, caseOption)

    # ORM결과를 json형태로 변환
    # pandas의 read_sql 함수를 사용(.all(), .first()같은 경우에는 예외처리)
    result = makeJsonWithCaseOption(results) 
    
    return Response(
        response = result,
        status = 200,
        mimetype="application/json"
    )

def testCase2(caseOption, data):
    # case_01_01 conditional query
    if caseOption=='01_01':
        conditions = []
        if data.get('GENDER', None) is not None:
                conditions.append(emp.gender == data['GENDER'])       
        if data.get('LOCATION', None) is not None:
                conditions.append(emp.location == data['LOCATION'])
        if data.get('DEPTNO', None) is not None:
            conditions.append(emp.deptno == data['DEPTNO'])
        results = db.session.query(emp).filter(and_(*conditions))
    return results

@app.route('/test_orm_post', methods=["POST"])
def test_orm_post():
    data = request.get_json()
    caseOption = request.args.get('case')
    results = testCase2(caseOption, data)

    # ORM에서 변환된 SQL문을 콘솔로 확인
    checkQueryInConsole(results, caseOption)

    # ORM결과를 json형태로 변환
    # pandas의 read_sql 함수를 사용(.all(), .first()같은 경우에는 예외처리)
    result = makeJsonWithCaseOption(results) 
    
    return Response(
        response = result,
        status = 200,
        mimetype="application/json"
    )

if __name__ == '__main__':
    app.run(host="192.168.0.51", port="5000", debug=True)
    # app.run(host="192.168.56.1", port="5000", debug=True)

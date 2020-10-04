case_01_01_단순 group query
    ㄴ mysql
        select count(id) from emp group by location
    ㄴ orm
        results = db.session.query(emp)\
            .with_entities(
                emp.location, 
                func.count(emp.id),
                func.count(emp.id).label('count') # label 사용 이유
            ).group_by(emp.location)
    
case_01_02_group query with distinct count
    ㄴ mysql
        SELECT gender, COUNT(gender), COUNT(DISTINCT location) FROM emp GROUP BY gender
    ㄴ orm
        results = db.session.query(emp)\
            .with_entities(
                emp.gender, 
                func.count(distinct(emp.location)), 
                func.count(emp.id)
            ).group_by(emp.gender)

case_02_having절을 포함한 group query
    ㄴ mysql
        select count(id), location from emp group by location HAVING COUNT(id)>2;
    ㄴ orm
        results = db.session.query(emp)\
            .with_entities(
                emp.location, 
                func.count(emp.id)
            ).group_by(emp.location)\
            .having(func.count(emp.id)>1)

case_03_order by절을 포함한 group query
    ㄴ mysql
        select count(id), location from emp group by location HAVING COUNT(id)>1 ORDER BY COUNT(id) desc;
    ㄴ orm
        results = db.session.query(emp)\
            .with_entities(
                emp.location, 
                func.count(emp.id)
            ).group_by(emp.location)\
            .having(func.count(emp.id)>1)\
            .order_by(func.count(emp.id).desc())

case_04 where절을 포함한 group query
    ㄴ mysql
        select count(id), location from emp WHERE gender = 'm' group by location HAVING COUNT(id)>1 ORDER BY COUNT(id) desc;
    ㄴ orm
        results = db.session.query(emp)\
            .filter(emp.gender=='m')\
            .with_entities(
                emp.location, 
                func.count(emp.id)
            ).group_by(emp.location)\
            .having(func.count(emp.id)>1)\
            .order_by(func.count(emp.id).desc())

case_05_01 다중 컬럼 group query
    ㄴ mysql
        SELECT COUNT(id), location, deptno FROM emp GROUP BY location, deptno;
    ㄴ orm
        results = db.session.query(emp)\
            .with_entities(
                func.count(emp.id), 
                emp.location, 
                emp.deptno
            ).group_by(emp.location, emp.deptno)

case_05_02 다중 컬럼 group query(지역, 연령별 평균연봉)
    ㄴ mysql
        SELECT location,concat(FLOOR(age/10), '0대' ) AS '연령대', AVG(salary) AS 'salary_average', count(id) FROM emp GROUP BY location, FLOOR(age/10);
    ㄴ orm
        results = db.session.query(emp)\
            .with_entities(
                func.count(emp.id).label('count'), 
                func.avg(emp.salary).label('salary_average'), 
                emp.location.label('location'), 
                (func.floor((emp.age)/10)*10).label('연령대별')
                ).group_by(
                    emp.location, 
                    func.floor((emp.age)/10))

case_06_01 추가적인예시(평균 대비 편차구하기)
    ㄴ mysql
        SELECT e.age-a.avg_age FROM emp e, (SELECT AVG(age) AS avg_age FROM emp) a
    ㄴ orm
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

case_06_02 추가적인예시(특정 조건의 전체자료 가져오기 )
    ㄴ mysql
        SELECT id, name FROM emp WHERE gender='m'
    ㄴ orm
        results = db.session.query(emp)\
            .filter(emp.gender=='m')\
            .with_entities(
                emp.id.label('id'), 
                emp.name.label('name')
            ).all()   

case_06_03 추가적인예시(특정 조건의 첫번쨰자료 가져오기 )
    ㄴ mysql
        SELECT id, name FROM emp WHERE gender='m' LIMIT 1
    ㄴ orm
        results =db.session.query(emp)\
            .filter(emp.gender=='m')\
                .with_entities(
                    emp.id, 
                    emp.name
                ).first()

case_06_04 scalar()를 활용한 조건검색(한가지 값을 검색하며 검색결과가 없거나 두개 이상일 경우 예외처리)
    ㄴ mysql
        SELECT id, name FROM emp WHERE gender='m' LIMIT 1
    ㄴ orm
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

case_06_05 추가적인예시(연령대(30대미만, 30대, 40대, 50대이상)별 평균연봉)
case-when을 사용하기 전 query
    ㄴ mysql
        SELECT tmp1.avg_sal AS '30대미만 평균연봉', tmp2.avg_sal AS '30대 평균연봉', tmp3.avg_sal AS '40대 평균연봉', tmp4.avg_sal AS '50대이상 평균연봉' FROM 
        (SELECT AVG(salary) AS avg_sal FROM emp WHERE age < 30) tmp1,
        (SELECT AVG(salary) AS avg_sal FROM emp WHERE age >=30 AND age <40) tmp2,
        (SELECT AVG(salary) AS avg_sal FROM emp WHERE age >=40 AND age <50) tmp3,
        (SELECT AVG(salary) AS avg_sal FROM emp WHERE age >= 50) tmp4    
    ㄴ orm
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

case_06_05_02 추가적인예시(연령대(30대미만, 30대, 40대, 50대이상)별 평균연봉) - case-when 사용
    ㄴ mysql
        select 
        avg(case when age<30 then salary end) as '30대 미만 연봉',
        avg(case when (age>=30 and age<40) then salary end) as '30대 연봉',
        avg(case when (age>=40 and age<50) then salary end) as '40대 연봉',
        avg(case when age>=50 then salary end) as '50대 이상 연봉'
        from emp;
    ㄴ orm
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

case_06_06 추가적인예시(전체나이 합계에 차지하는 개별나이의 비율) - subquery
    ㄴ mysql
        SELECT a.age AS age, a.age*a.countid/b.agesum*100 as rate FROM
        (SELECT COUNT(id) AS countid, age FROM emp GROUP BY age) a,
        (SELECT SUM(age) AS agesum FROM emp) b;    
    ㄴ orm
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

case_07_01 null검색
    ㄴ mysql
        select * from board where content is null;
    ㄴ orm
        results = db.session.query(board)\
            .with_entities(
                board.id, 
                board.writer_id, 
                board.title, 
                board.content
            ).filter(board.content == None)

case_07_02_01 '' 검색
    ㄴ mysql
        select * from board where content is '';
    ㄴ orm
        results = db.session.query(board)\
            .with_entities(
                board.id, 
                board.writer_id, 
                board.title, 
                board.content
            ).filter(board.content == '')

case_07_02_02 ' ' 검색
    ㄴ mysql
        select * from board where content is ' ';
    ㄴ orm
        results = db.session.query(board)\
            .with_entities(
                board.id, 
                board.writer_id, 
                board.title, 
                board.content
            ).filter(board.content == ' ')

case_07_03 ifnull()
    ㄴ mysql
        select id, writer_id, title, ifnull(content, 'default_board_content') as content from board where content is null;
    ㄴ orm
        results = db.session.query(board)\
            .with_entities(
                board.id, 
                board.writer_id, 
                board.title, 
                func.ifnull(board.content, 'default_board_content').label('content')
            ).filter(board.content == None)

case_07_04 between()
    ㄴ mysql
        select * from board where id >=5 and id<=10;
    ㄴ orm
        results = db.session.query(board)\
            .with_entities(
                board.id, 
                board.writer_id, 
                board.title, 
                board.content
            ).filter(between(board.id, 5, 10))

case_07_05 like()
    ㄴ mysql
        select * from board where content like '%aaa%';
    ㄴ orm
        results = db.session.query(board)\
            .with_entities(
                board.id, 
                board.writer_id, 
                board.title, 
                board.content
            ).filter(board.content.like("%aaa%"))
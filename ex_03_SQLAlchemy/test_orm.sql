CREATE TABLE emp(
	id INT,
	name varchar(128),
	gender varchar(16),
	age INT,
	location varchar(32),
	deptno INT,
    hiredate date,
    salary INT
);
INSERT INTO emp(id, name, gender, age, location, deptno, hiredate, salary) VALUES(1, 'aaa', 'm', 21, 'seoul', 11, '2005-03-02', 15000);
INSERT INTO emp(id, name, gender, age, location, deptno, hiredate, salary) VALUES(2, 'bbb', 'w', 25, 'seoul', 12, '2011-02-05', 12000);
INSERT INTO emp(id, name, gender, age, location, deptno, hiredate, salary) VALUES(3, 'ccc', 'm', 30, 'busan', 11, '2020-03-20', 10000);
INSERT INTO emp(id, name, gender, age, location, deptno, hiredate, salary) VALUES(4, 'ddd', 'w', 40, 'seoul', 12, '2020-05-05', 20000);
INSERT INTO emp(id, name, gender, age, location, deptno, hiredate, salary) VALUES(5, 'ee', 'w', 30, 'seongnam', 21, '2016-04-24', 14000);
INSERT INTO emp(id, name, gender, age, location, deptno, hiredate, salary) VALUES(6, 'fff', 'm', 20, 'seoul', 22, '2005-03-23', 13000);
INSERT INTO emp(id, name, gender, age, location, deptno, hiredate, salary) VALUES(7, 'ggg', 'w', 44, 'seongnam', 31, '1999-02-22', 40000);
INSERT INTO emp(id, name, gender, age, location, deptno, hiredate, salary) VALUES(8, 'hhh', 'm', 60, 'busan', 11, '2010-03-03', 22000);
INSERT INTO emp(id, name, gender, age, location, deptno, hiredate, salary) VALUES(9, 'iii', 'm', 36, 'incheon', 21, '2015-05-15', 25000);





/*
case_01_01_단순 group query
	ㄴ mysql : select count(id) from emp group by location
	ㄴ orm : emp.query.with_entities(emp.location, func.count(emp.id)).group_by(emp.location)
case_01_02_group query with distinct count
	ㄴ mysql : SELECT gender, COUNT(gender), COUNT(DISTINCT location) FROM emp GROUP BY gender
	ㄴ orm : emp.query.with_entities(emp.gender, func.count(distinct(emp.location)), func.count(emp.id)).group_by(emp.gender)
case_02_having절을 포함한 group query
	ㄴ mysql : select count(id), location from emp group by location HAVING COUNT(id)>2;
	ㄴ orm : emp.query.with_entities(emp.location, func.count(emp.id)).group_by(emp.location).having(func.count(emp.id)>2)
case_03_order by절을 포함한 group query
	ㄴ mysql : select count(id), location from emp group by location HAVING COUNT(id)>1 ORDER BY COUNT(id) desc;
	ㄴ orm : emp.query.with_entities(emp.location, func.count(emp.id)).group_by(emp.location).having(func.count(emp.id)>1).order_by(func.count(emp.id).desc())
case_04 where절을 포함한 group query
	ㄴ .filter와 .with_entities의 순서가 의미없는듯 **
	ㄴ mysql : select count(id), location from emp WHERE gender = 'm' group by location HAVING COUNT(id)>1 ORDER BY COUNT(id) desc;
	ㄴ orm : emp.query.filter(emp.gender=='m').with_entities(emp.location, func.count(emp.id)).group_by(emp.location).having(func.count(emp.id)>1).order_by(func.count(emp.id).desc())
case_05_01 다중 컬럼 group query
	ㄴ mysql : SELECT COUNT(id), location, deptno FROM emp GROUP BY location, deptno;
	ㄴ orm : emp.query.with_entities(func.count(emp.id), emp.location, emp.deptno).group_by(emp.location, emp.deptno)
case_05_02 다중 컬럼 group query(지역, 연령별 평균연봉)
	ㄴ mysql : SELECT location,concat(FLOOR(age/10), '0대' ) AS '연령대', AVG(salary) AS 'salary_average', count(id) FROM emp GROUP BY location, FLOOR(age/10);
	ㄴ orm : results = emp.query.with_entities(func.count(emp.id).label('count'), func.avg(emp.salary).label('salary_average'), emp.location.label('location'), (func.floor((emp.age)/10)*10).label('연령대별')).group_by(emp.location, func.floor((emp.age)/10))
case_06_01 추가적인예시(평균 대비 편차구하기)
	ㄴ mysql : SELECT e.age-a.avg_age FROM emp e, (SELECT AVG(age) AS avg_age FROM emp) a
	ㄴ orm : avg_age = emp.query.with_entities(func.avg(emp.age).label('age')).first()
			 results = emp.query.with_entities((emp.age-avg_age).label('평균나이 별 편차'), emp.age, emp.id)
case_06_02 추가적인예시(특정 조건의 전체자료 가져오기 )
	ㄴ mysql : SELECT * FROM emp WHERE gender='m'
	ㄴ orm : emp.query.filter(emp.gender=='m').all()    
case_06_03 추가적인예시(특정 조건의 첫번쨰자료 가져오기 )
	ㄴ mysql : SELECT * FROM emp WHERE gender='m' LIMIT 1
	ㄴ orm : emp.query.filter(emp.gender=='m').first()
case_06_04 scalar()를 활용한 조건검색(한가지 값을 검색하며 검색결과가 없거나 두개 이상일 경우 예외처리)
	ㄴ mysql : SELECT * FROM emp WHERE gender='m' LIMIT 1
	ㄴ orm :     
	try:
        results = emp.query.filter(emp.gender=='m').scalar()    
	    print(results)
	except NoResultFound:
		print('결과값이 존재하지 않습니다.')
	except MultipleResultsFound:
		print('두개 이상의 결과가 발견되었습니다.')
case_06_05 추가적인예시(연령대(30대미만, 30대, 40대, 50대이상)별 평균연봉)
	ㄴ mysql : 
	SELECT tmp1.avg_sal AS '30대미만 평균연봉', tmp2.avg_sal AS '30대 평균연봉', tmp3.avg_sal AS '40대 평균연봉', tmp4.avg_sal AS '50대이상 평균연봉' FROM 
	(SELECT AVG(salary) AS avg_sal FROM emp WHERE age < 30) tmp1,
	(SELECT AVG(salary) AS avg_sal FROM emp WHERE age >=30 AND age <40) tmp2,
	(SELECT AVG(salary) AS avg_sal FROM emp WHERE age >=40 AND age <50) tmp3,
	(SELECT AVG(salary) AS avg_sal FROM emp WHERE age >= 50) tmp4    
	ㄴ orm : 
    tmp1 = emp.query.with_entities(func.avg(emp.salary).label('avg_sal')).filter(emp.age<30).one()
    tmp2 = emp.query.with_entities(func.avg(emp.salary).label('avg_sal')).filter(emp.age>=30).filter(emp.age<40).one()
    tmp3 = emp.query.with_entities(func.avg(emp.salary).label('avg_sal')).filter(emp.age>=40).filter(emp.age<50).one()
    tmp4 = emp.query.with_entities(func.avg(emp.salary).label('avg_sal')).filter(emp.age>=50).one()
    results = {'30대미만 평균연봉': tmp1.avg_sal, '30대 평균연봉':tmp2.avg_sal, '40대 평균연봉':tmp3.avg_sal, '50대이상 평균연봉':tmp4.avg_sal}
case_06_06 추가적인예시(전체나이 합계에 차지하는 개별나이의 비율)
	ㄴ mysql :
	SELECT a.age AS age, a.age*a.countid/b.agesum*100 as rate FROM
	(SELECT COUNT(id) AS countid, age FROM emp GROUP BY age) a,
	(SELECT SUM(age) AS agesum FROM emp) b;
	ㄴ orm :
    subq1 = db.session.query(emp).with_entities(func.count(emp.id).label('countid'), emp.age.label('age')).group_by(emp.age).subquery()
    subq2 = db.session.query(emp).with_entities(func.sum(emp.age).label('agesum')).subquery()
    results = db.session.query(subq1, subq2).with_entities(subq1.c.age, (subq1.c.age*subq1.c.countid/subq2.c.agesum*100).label('rate'))
*/
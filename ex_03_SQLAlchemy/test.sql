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
case_01_단순 group query
	ㄴ mysql : select count(id) from emp group by location
	ㄴ orm : emp.query.with_entities(emp.location, func.count(emp.id)).group_by(emp.location)
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
	ㄴ orm : emp.query.with_entities(func.count(emp.id).label('count'), func.avg(emp.salary).label('salary_average'), emp.location, (func.floor((emp.age)/10)*10).label('연령대')).group_by(emp.location, func.floor((emp.age)/10))
case_06 subquery (평균 대비 편차구하기)
	ㄴ mysql : SELECT e.age-a.avg_age FROM emp e, (SELECT AVG(age) AS avg_age FROM emp) a
	ㄴ orm : avg_age = emp.query.with_entities(func.avg(emp.age).label('age')).first()
			 results = emp.query.with_entities((emp.age-avg_age).label('평균나이 별 편차'), emp.age, emp.id)
case_07_01 추가적인예시(특정 조건의 전체자료 가져오기 )
	ㄴ mysql : SELECT * FROM emp WHERE gender='m'
	ㄴ orm : emp.query.filter(emp.gender=='m').all()    
case_07_02 추가적인예시(특정 조건의 첫번쨰자료 가져오기 )
	ㄴ mysql : SELECT * FROM emp WHERE gender='m' LIMIT 1
	ㄴ orm : emp.query.filter(emp.gender=='m').first()    
*/
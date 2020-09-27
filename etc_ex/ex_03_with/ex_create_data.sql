-- 샘플데이터1 구조
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

-- 샘플데이터1 데이터
INSERT INTO emp(id, name, gender, age, location, deptno, hiredate, salary) VALUES(1, 'aaa', 'm', 21, 'seoul', 11, '2005-03-02', 15000);
INSERT INTO emp(id, name, gender, age, location, deptno, hiredate, salary) VALUES(2, 'bbb', 'w', 25, 'seoul', 12, '2011-02-05', 12000);
INSERT INTO emp(id, name, gender, age, location, deptno, hiredate, salary) VALUES(3, 'ccc', 'm', 30, 'busan', 11, '2020-03-20', 10000);
INSERT INTO emp(id, name, gender, age, location, deptno, hiredate, salary) VALUES(4, 'ddd', 'w', 40, 'seoul', 12, '2020-05-05', 20000);
INSERT INTO emp(id, name, gender, age, location, deptno, hiredate, salary) VALUES(5, 'ee', 'w', 30, 'seongnam', 21, '2016-04-24', 14000);
INSERT INTO emp(id, name, gender, age, location, deptno, hiredate, salary) VALUES(6, 'fff', 'm', 20, 'seoul', 22, '2005-03-23', 13000);
INSERT INTO emp(id, name, gender, age, location, deptno, hiredate, salary) VALUES(7, 'ggg', 'w', 44, 'seongnam', 31, '1999-02-22', 40000);
INSERT INTO emp(id, name, gender, age, location, deptno, hiredate, salary) VALUES(8, 'hhh', 'm', 60, 'busan', 11, '2010-03-03', 22000);
INSERT INTO emp(id, name, gender, age, location, deptno, hiredate, salary) VALUES(9, 'iii', 'm', 36, 'incheon', 21, '2015-05-15', 25000);

-- 샘플데이터2 구조
-- clob(oracle) <-> longtext(mysql)
create table board(
	id int,
	writer_id varchar(64),
	title varchar(128),
	content longtext
);

-- 샘플데이터2 데이터
INSERT INTO board(id, writer_id, title, content) VALUES (1, 'abc123', 'title1', 'content1');
INSERT INTO board(id, writer_id, title, content) VALUES (2, 'abc123', 'title2', 'content2');
INSERT INTO board(id, writer_id, title, content) VALUES (3, 'abc1230', 'title3', 'content3');
INSERT INTO board(id, writer_id, title, content) VALUES (4, 'abc1230', 'title4', 'content4');
INSERT INTO board(id, writer_id, title, content) VALUES (5, 'abc12300', 'title5', 'content5');
INSERT INTO board(id, writer_id, title, content) VALUES (6, 'abc1239', 'title6', 'content6');
INSERT INTO board(id, writer_id, title, content) VALUES (7, 'abc1238', 'title7', 'content7');
INSERT INTO board(id, writer_id, title, content) VALUES (8, 'abc1237', 'title8', 'content8');
INSERT INTO board(id, writer_id, title, content) VALUES (9, 'abc1236', 'title9', 'content9');
INSERT INTO board(id, writer_id, title) VALUES (10, 'abc1235', 'title10');
INSERT INTO board(id, writer_id, title, content) VALUES (11, 'abc1234', 'title11', '');
INSERT INTO board(id, writer_id, title, content) VALUES (12, 'abc1234', 'title12', ' ');
INSERT INTO board(id, writer_id, title) VALUES (13, 'abc1235', 'title13');
INSERT INTO board(id, writer_id, title) VALUES (14, 'abc1235', 'title14');
INSERT INTO board(id, writer_id, title) VALUES (15, 'abc1235', 'title15');
INSERT INTO board(id, writer_id, title, content) VALUES (16, 'abc12345', 'title16', '');
INSERT INTO board(id, writer_id, title, content) VALUES (17, 'abc12346', 'title17', ' ');
INSERT INTO board(id, writer_id, title, content) VALUES (18, 'abc12300', 'title18', 'aaa content');
INSERT INTO board(id, writer_id, title, content) VALUES (19, 'abc1239', 'title18', 'aaa');
INSERT INTO board(id, writer_id, title, content) VALUES (20, 'abc1238', 'title18', 'aaa ddd');
INSERT INTO board(id, writer_id, title, content) VALUES (21, 'abc1237', 'title18', 'aaa bbb');
INSERT INTO board(id, writer_id, title, content) VALUES (22, 'abc1237', 'title18', 'aaa ccc');

/*
----- with절 사용 방법 -----
CTE => Common Table Expression
CTE(Common Table Expression)는 서브쿼리로 쓰이는 파생테이블(derived table)과 비슷한 개념으로 사용된다.
CTE와 비교대상으로는 VIEW가 있다. VIEW는 만들기 위해 권한이 필요하고 사전에 정의를 해야한다. 반면, CTE는 권한이 필요 없고 하나의 쿼리문이 끝날때까지만 지속되는 일회성 테이블이다.
CTE는 주로 복잡한 쿼리문에서 코드의 가독성과 재사용성을 위해 파생테이블 대신 사용하기에 유용하다.
CTE에는 재귀적 CTE와 비재귀적 CTE가 있지만 여기서는 다루지 않는다.
참고 : MySQL은 8.0부터 지원한다.

1. WITH구문 - 1개만 있을 때
WITH ALIAS명 AS ( SUB쿼리 ) 
SELECT 컬럼명 FROM ALIAS명;

2. WITH구문 - 여러개(2개 이상)
WITH [WITH절 명칭-1] AS (SELECT [컬럼명-1] FROM [테이블명-1]),
        [WITH절 명칭-2] AS (SELECT [컬럼명-2] FROM [테이블명-2])
SELECT ALIAS명-1.[컬럼명-1]
        , ALIAS명-2.[컬럼명-2]
FROM [WITH절 명칭-1] ALIAS명-1 
       ,  [WITH절 명칭-2] ALIAS명-2

[1. 예제를 위한 테이블 생성, 데이터 삽입]

CREATE TABLE TAB1 (NO NUMBER, COL1 VARCHAR2(20), COL2 VARCHAR2(20));
CREATE TABLE TAB2 (NO NUMBER, COL1 VARCHAR2(20), COL2 VARCHAR2(20));
CREATE TABLE TAB3 (NO NUMBER, COL1 VARCHAR2(20), COL2 VARCHAR2(20));

INSERT INTO TAB1 (NO,COL1,COL2) VALUES(1,'AAA','가');
INSERT INTO TAB1 (NO,COL1,COL2) VALUES(2,'BBB','나');
INSERT INTO TAB1 (NO,COL1,COL2) VALUES(3,'CCC','다');
INSERT INTO TAB2 (NO,COL1,COL2) VALUES(1,'DDD','라');
INSERT INTO TAB2 (NO,COL1,COL2) VALUES(2,'EEE','마');
INSERT INTO TAB2 (NO,COL1,COL2) VALUES(3,'FFF','바');
INSERT INTO TAB3 (NO,COL1,COL2) VALUES(1,'GGG','사');
INSERT INTO TAB3 (NO,COL1,COL2) VALUES(2,'HHH','아');
INSERT INTO TAB3 (NO,COL1,COL2) VALUES(3,'III','자');

[2. WITH구문 - 1개만 있을 때]

WITH  WITH_TAB
     AS (SELECT NO, COL1
         FROM   TAB1
         WHERE  NO = 1
)
select  C.NO AS TAB1_NO
     , C.COL1 AS TAB1_COL1
     , A.COL1 AS TAB2_COL1
     , A.COL2 AS TAB2_COL2
     , B.COL1 AS TAB3_COL1
     , B.COL2 AS TAB3_COL2
from TAB2 A, TAB3 B, WITH_TAB C
where A.NO = B.NO;

[3. WITH구문 - 여러개(2개 이상)]

WITH  WITH_TAB1
  AS (SELECT NO, COL1, COL2
      FROM TAB1)
   ,  WITH_TAB2
  AS (SELECT NO, COL1, COL2
      FROM TAB2)
   ,  WITH_TAB3
  AS (SELECT NO, COL1, COL2
      FROM TAB3)
select A.NO TAB1_NO
     , A.COL1 TAB1_COL1
     , A.COL2 TAB1_COL2
     , B.NO TAB2_NO
     , B.COL1 TAB2_COL1
     , B.COL2 TAB2_COL2
     , C.NO TAB3_NO
     , C.COL1 TAB3_COL1
     , C.COL2 TAB3_COL2
from WITH_TAB1 A, WITH_TAB2 B, WITH_TAB3 C
where A.NO = B.NO
AND   A.NO = C.NO;
*/
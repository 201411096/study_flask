-- 사용방법 (INFORMATION_SCHEMA를 이용한 .. 컴럼들의 정보들을 가져오기)
-- SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS
-- WHERE table_schema = 'your_db_name ...'
-- AND TABLE_NAME = 'your_table_name ...';

-- 사용예시1 (INFORMATION_SCHEMA를 이용한 .. 컬럼들의 이름과 데이터 타입 정보 가져오기)
-- SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS
-- WHERE table_schema = 'test'
-- AND TABLE_NAME = 'test';

-- 사용예시2 (INFORMATION_SCHEMA를 이용한 .. 컬럼의 정보를 가져오기)
-- SELECT DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS
-- WHERE table_schema = 'test'
-- AND TABLE_NAME = 'test'
-- AND COLUMN_NAME = 'id';

-- 사용예시2 (INFORMATION_SCHEMA를 이용한 .. 테이블의 컬럼 정보들 가져오기)
-- SELECT * FROM INFORMATION_SCHEMA.COLUMNS
-- WHERE table_schema = 'test'
-- AND TABLE_NAME = 'test';

--사용방법 (INFORMATION_SCHEMA를 이용한 .. 테이블 리스트들을 가져오기)
select table_name
from information_schema.TABLES
where table_schema = 'your_db_name'

-- 사용방법 (show query ..)
--show COLUMNS FROM your_tableName FROM your_dbName WHERE FIELD ='your_columnName ...';

-- 사용예시1 (show query ..)
--show COLUMNS FROM test FROM test WHERE FIELD ='id';
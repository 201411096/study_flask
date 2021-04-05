CREATE TABLE kys(
	col_date DATE,
	col_text TEXT,
	col_int INT,
	col_string VARCHAR(128),
	col_numeric double(10,2),
	col_bit BIT(10)
);
COMMIT;
INSERT INTO kys (col_date, col_text, col_int, col_string, col_numeric, col_bit)
VALUE(NOW(), 'testtext1', '11', 'test-string', 123.12, 01010);
select * from kys
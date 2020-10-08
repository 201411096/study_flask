CREATE TABLE RecursionTest 
( 
id INTEGER NOT NULL, 
name VARCHAR(128) NULL, 
parent INTEGER NULL, 
CONSTRAINT pk_RecursionTest PRIMARY KEY (id) 
); 
 
INSERT INTO RecursionTest (id, name, parent) VALUES (1, 'Root', NULL); 
INSERT INTO RecursionTest (id, name, parent) VALUES (2, 'Branch A', 1); 
INSERT INTO RecursionTest (id, name, parent) VALUES (3, 'Branch B', 1); 
INSERT INTO RecursionTest (id, name, parent) VALUES (4, 'Branch C', 1); 
INSERT INTO RecursionTest (id, name, parent) VALUES (5, 'Branch A2', 2); 
INSERT INTO RecursionTest (id, name, parent) VALUES (6, 'Branch B2', 3); 
INSERT INTO RecursionTest (id, name, parent) VALUES (7, 'Branch B3', 6); 
INSERT INTO RecursionTest (id, name, parent) VALUES (8, 'Branch B4', 7);

with recursive cte (id, name, parent) as
(
 select     id,
            name,
            parent
 from       recursiontest
 where      parent = 3
 union all
 select     r.id,
            r.name,
            r.parent
 from       recursiontest r
 inner join cte
         on r.parent = cte.id
)
 
select * from cte;
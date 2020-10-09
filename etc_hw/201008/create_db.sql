create table tree_table(
    id int(11) primary key,
    pid int(11),
    NAME varchar(20),
    description varchar(500)
);

insert into tree_table(id, pid, NAME, description) values (1, 0, 'node1', 'des_01');
insert into tree_table(id, pid, NAME, description) values (2, 1, 'node2', 'des_02');
insert into tree_table(id, pid, NAME, description) values (3, 1, 'node3', 'des_03');
insert into tree_table(id, pid, NAME, description) values (4, 2, 'node4', 'des_04');
insert into tree_table(id, pid, NAME, description) values (5, 2, 'node5', 'des_05');
insert into tree_table(id, pid, NAME, description) values (6, 3, 'node6', 'des_06');
insert into tree_table(id, pid, NAME, description) values (7, 3, 'node7', 'des_07');
insert into tree_table(id, pid, NAME, description) values (8, 4, 'node8', 'des_08');
insert into tree_table(id, pid, NAME, description) values (9, 4, 'node9', 'des_09');
insert into tree_table(id, pid, NAME, description) values (10, 5, 'node10', 'des_010');
insert into tree_table(id, pid, NAME, description) values (11, 5, 'node11', 'des_011');
insert into tree_table(id, pid, NAME, description) values (12, 6, 'node12', 'des_012');
insert into tree_table(id, pid, NAME, description) values (13, 6, 'node13', 'des_013');
insert into tree_table(id, pid, NAME, description) values (14, 1, 'node14', 'des_014');
insert into tree_table(id, pid, NAME, description) values (15, 0, 'node15', 'des_015');
insert into tree_table(id, pid, NAME, description) values (16, 2, 'node16', 'des_016');
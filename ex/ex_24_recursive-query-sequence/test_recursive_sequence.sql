CREATE TABLE IF NOT EXISTS `test_recursive` (
  `id` int(11) NOT NULL,
  `pid` int(11) DEFAULT NULL,
  `nm` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT IGNORE INTO `test_recursive` (`id`, `pid`, `nm`) VALUES
	(1, 0, 'root'),
	(2, 1, 'A'),
	(3, 1, 'B'),
	(4, 1, 'C'),
	(5, 2, 'AA'),
	(6, 2, 'AB'),
	(7, 2, 'AC'),
	(8, 5, 'AAA'),
	(9, 5, 'AAB'),
	(10, 5, 'AAC'),
	(11, 6, 'ABA'),
	(12, 2, 'ABB'),
	(13, 8, 'AAAA'),
	(14, 0, 'xxx'),
	(15, 14, 'XXXX'),
	(16, 1, 'XX-A');


# 예시1 => lvl2를 이용한 정렬이 정상적인 정렬
with recursive cte as
(
 select     id,
            nm,
            pid,
            0 AS depth,
            CAST(id AS VARCHAR(1000)) as lvl,
            CAST(LPAD(id, 10, "0") AS VARCHAR(1000)) as lvl2
 from       test_recursive
 where      pid = 0
 union all
 select     r.id,
            r.nm,
            r.pid,
            1 + depth AS depth,
            CONCAT(cte.lvl, "-", r.id) as lvl,
            CONCAT(cte.lvl2, "-", LPAD(r.id, 10, "0")) as lvl2
 from       test_recursive r
 inner join cte
         on r.pid = cte.id
)
select * from cte
ORDER BY lvl2;

# 예시2
with recursive cte as
(
 select     id,
            nm,
            pid,
            0 AS depth,
            CAST(LPAD(id, 10, "0") AS VARCHAR(1000)) as lvl
 from       test_recursive
 where      pid = 0
 union all
 select     r.id,
            r.nm,
            r.pid,
            1 + depth AS depth,
            CONCAT(cte.lvl, "-", LPAD(r.id, 10, "0")) as lvl
 from       test_recursive r
 inner join cte
         on r.pid = cte.id
)
select * from cte
ORDER BY lvl;


#예시3 그룹별 정렬 후 그룹내에서 lvl별 정렬(게시판)
with recursive cte as
(
 select     id,
            nm,
            pid,
            0 AS depth,
            CAST(LPAD(id, 10, "0") AS VARCHAR(1000)) as grp,
            CAST(LPAD(id, 10, "0") AS VARCHAR(1000)) as lvl
 from       test_recursive
 where      pid = 0
 union all
 select     r.id,
            r.nm,
            r.pid,
            1 + depth AS depth,
            grp AS grp,
            CONCAT(cte.lvl, "-", LPAD(r.id, 10, "0")) as lvl
 from       test_recursive r
 inner join cte
         on r.pid = cte.id
)
select * from cte
ORDER BY grp desc, lvl;

#예시4_1 그룹별 정렬 후 그룹내에서 lvl별 정렬(게시판) + 게시판별 넘버링
with recursive cte as
(
 select     id,
            nm,
            pid,
            0 AS depth,
            CAST(LPAD(id, 10, "0") AS VARCHAR(1000)) as grp,
            CAST(LPAD(id, 10, "0") AS VARCHAR(1000)) as lvl
 from       test_recursive
 where      pid = 0
 union all
 select     r.id,
            r.nm,
            r.pid,
            1 + depth AS depth,
            grp AS grp,
            CONCAT(cte.lvl, "-", LPAD(r.id, 10, "0")) as lvl
 from       test_recursive r
 inner join cte
         on r.pid = cte.id
)
SELECT * FROM
(SELECT * FROM
(SELECT @ROWNUM:=@ROWNUM+1 AS number, c.* 
FROM cte c, 
(SELECT @ROWNUM:=0) b ORDER BY id) t 
) a 
ORDER BY grp DESC, lvl;

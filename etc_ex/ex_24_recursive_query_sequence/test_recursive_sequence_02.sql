-- --------------------------------------------------------
-- 호스트:                          192.168.0.13
-- 서버 버전:                        10.5.5-MariaDB - mariadb.org binary distribution
-- 서버 OS:                        Win64
-- HeidiSQL 버전:                  11.0.0.5919
-- --------------------------------------------------------
-- board 구조 변경 후
/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- kimyongseon 데이터베이스 구조 내보내기
CREATE DATABASE IF NOT EXISTS `kimyongseon` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `kimyongseon`;

-- 테이블 kimyongseon.board 구조 내보내기
CREATE TABLE IF NOT EXISTS `board` (
  `board_content_id` int(11) NOT NULL AUTO_INCREMENT,
  `board_content_pid` varchar(100) DEFAULT NULL,
  `member_id` varchar(100) DEFAULT NULL,
  `board_id` varchar(100) DEFAULT NULL,
  `board_content_title` varchar(100) DEFAULT NULL,
  `board_content_body` varchar(1000) DEFAULT NULL,
  `board_content_regdatetime` datetime DEFAULT NULL,
  `board_content_edtdatetime` datetime DEFAULT NULL,
  `board_content_num` varchar(100) DEFAULT NULL,
  `board_content_deleted` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`board_content_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

-- 테이블 데이터 kimyongseon.board:~10 rows (대략적) 내보내기
/*!40000 ALTER TABLE `board` DISABLE KEYS */;
INSERT IGNORE INTO `board` (`board_content_id`, `board_content_pid`, `member_id`, `board_id`, `board_content_title`, `board_content_body`, `board_content_regdatetime`, `board_content_edtdatetime`, `board_content_num`, `board_content_deleted`) VALUES
	(1, '-1', 'abc', '01', 'aa', 'aa', '2021-01-20 15:31:29', '2021-01-20 15:31:29', NULL, 'N'),
	(2, '-1', 'abc', '01', 'bb', 'bb', '2021-01-20 15:51:50', '2021-01-20 15:51:50', NULL, 'N'),
	(3, '2', 'abc', '01', 'rebb', 'bb', '2021-01-20 15:52:02', '2021-01-20 15:52:02', NULL, 'N'),
	(4, '3', 'abc', '01', 'rerebb', 'ree', '2021-01-20 15:54:44', '2021-01-20 15:54:44', NULL, 'N'),
	(5, '-1', 'abc', '01', 'cc', 'cc', '2021-01-20 15:59:23', '2021-01-20 15:59:23', NULL, 'N'),
	(6, '2', 'abc', '01', 're2bbb', 'bbb', '2021-01-20 15:59:41', '2021-01-20 15:59:41', NULL, 'N'),
	(7, '-1', 'abc', '01', 'bbb', 'bbb', '2021-01-20 16:00:19', '2021-01-20 16:00:19', NULL, 'N'),
	(8, '-1', 'abc', '02', 'dd', 'dd', '2021-01-20 16:00:26', '2021-01-20 16:00:26', NULL, 'N'),
	(9, '-1', 'abc', '01', 'ee', 'ee', '2021-01-20 16:00:32', '2021-01-20 16:00:32', NULL, 'N'),
	(10, '9', 'abc', '01', 'reaa', 're', '2021-01-20 16:00:42', '2021-01-20 16:00:42', NULL, 'N');
/*!40000 ALTER TABLE `board` ENABLE KEYS */;

-- 테이블 kimyongseon.board_list 구조 내보내기
CREATE TABLE IF NOT EXISTS `board_list` (
  `board_id` varchar(100) NOT NULL,
  `board_name` varchar(100) DEFAULT NULL,
  `board_des` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`board_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 테이블 데이터 kimyongseon.board_list:~5 rows (대략적) 내보내기
/*!40000 ALTER TABLE `board_list` DISABLE KEYS */;
INSERT IGNORE INTO `board_list` (`board_id`, `board_name`, `board_des`) VALUES
	('01', 'board_01', 'board_01_des'),
	('02', 'board_02', 'board_02_des'),
	('03', 'board_03', 'board_03_des'),
	('04', 'board_04', 'board_04_des'),
	('05', 'board_05', NULL);
/*!40000 ALTER TABLE `board_list` ENABLE KEYS */;

-- 테이블 kimyongseon.comment 구조 내보내기
CREATE TABLE IF NOT EXISTS `comment` (
  `comment_id` int(11) NOT NULL AUTO_INCREMENT,
  `comment_pid` varchar(100) DEFAULT NULL,
  `member_id` varchar(100) DEFAULT NULL,
  `board_content_id` varchar(100) DEFAULT NULL,
  `comment_body` varchar(1000) DEFAULT NULL,
  `comment_regdatetime` datetime DEFAULT NULL,
  `comment_edtdatetime` datetime DEFAULT NULL,
  `comment_deleted` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`comment_id`)
) ENGINE=InnoDB AUTO_INCREMENT=45 DEFAULT CHARSET=utf8;

-- 테이블 데이터 kimyongseon.comment:~0 rows (대략적) 내보내기
/*!40000 ALTER TABLE `comment` DISABLE KEYS */;
/*!40000 ALTER TABLE `comment` ENABLE KEYS */;

-- 테이블 kimyongseon.file 구조 내보내기
CREATE TABLE IF NOT EXISTS `file` (
  `file_id` varchar(100) NOT NULL,
  `board_content_id` varchar(100) DEFAULT NULL,
  `member_id` varchar(100) DEFAULT NULL,
  `file_name` varchar(100) DEFAULT NULL,
  `file_path` varchar(100) DEFAULT NULL,
  `file_type` varchar(100) DEFAULT NULL,
  `file_regdatetime` datetime DEFAULT NULL,
  `file_edtdatetime` datetime DEFAULT NULL,
  PRIMARY KEY (`file_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 테이블 데이터 kimyongseon.file:~0 rows (대략적) 내보내기
/*!40000 ALTER TABLE `file` DISABLE KEYS */;
/*!40000 ALTER TABLE `file` ENABLE KEYS */;

-- 테이블 kimyongseon.group_authority 구조 내보내기
CREATE TABLE IF NOT EXISTS `group_authority` (
  `group_code` varchar(100) NOT NULL,
  `authority_board_create` varchar(10) DEFAULT NULL,
  `authority_board_update` varchar(10) DEFAULT NULL,
  `authority_board_delete` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`group_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 테이블 데이터 kimyongseon.group_authority:~0 rows (대략적) 내보내기
/*!40000 ALTER TABLE `group_authority` DISABLE KEYS */;
/*!40000 ALTER TABLE `group_authority` ENABLE KEYS */;

-- 테이블 kimyongseon.group_board_authority 구조 내보내기
CREATE TABLE IF NOT EXISTS `group_board_authority` (
  `group_code` varchar(100) DEFAULT NULL,
  `board_id` varchar(100) DEFAULT NULL,
  `authority_board_content_read` varchar(10) DEFAULT NULL,
  `authority_board_content_write` varchar(10) DEFAULT NULL,
  `authority_board_content_update` varchar(10) DEFAULT NULL,
  `authority_board_content_delete` varchar(10) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 테이블 데이터 kimyongseon.group_board_authority:~0 rows (대략적) 내보내기
/*!40000 ALTER TABLE `group_board_authority` DISABLE KEYS */;
/*!40000 ALTER TABLE `group_board_authority` ENABLE KEYS */;

-- 테이블 kimyongseon.member 구조 내보내기
CREATE TABLE IF NOT EXISTS `member` (
  `member_id` varchar(100) NOT NULL,
  `group_code` varchar(100) DEFAULT NULL,
  `member_pw` varchar(100) DEFAULT NULL,
  `member_name` varchar(100) DEFAULT NULL,
  `member_birthday` datetime DEFAULT NULL,
  `member_phonenumber` varchar(100) DEFAULT NULL,
  `member_nickname` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`member_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 테이블 데이터 kimyongseon.member:~10 rows (대략적) 내보내기
/*!40000 ALTER TABLE `member` DISABLE KEYS */;
INSERT IGNORE INTO `member` (`member_id`, `group_code`, `member_pw`, `member_name`, `member_birthday`, `member_phonenumber`, `member_nickname`) VALUES
	('abc', '01', 'abc', 'abcname', '2021-01-12 00:00:00', '11', 'abcnname'),
	('admin', '00', 'admin', 'admin_name', '2021-01-15 13:18:22', '111111', 'admin_nickname'),
	('bcd', '01', 'bcd', '123', '2021-01-11 00:00:00', '12312', '123'),
	('cde', '01', 'cde', 'cddd', '2021-01-05 00:00:00', '111', '111'),
	('eee', '01', 'eee', 'eeee', '2021-01-06 00:00:00', '111', '123'),
	('ef', '01', 'ef', 'ef', '2020-12-29 00:00:00', 'ef', 'ef'),
	('fff', '01', '123', '123', '2021-01-04 00:00:00', '123', '123'),
	('ggg', '01', '123', '123', '2021-01-15 00:00:00', '123', '213'),
	('ggg1', '01', '123', 'dd', '2021-01-14 00:00:00', 'dd', 'dd'),
	('가나다', '01', '가나다', '간다ㅏ', '2021-01-16 00:00:00', 'ㅇ', 'ㅇ');
/*!40000 ALTER TABLE `member` ENABLE KEYS */;

-- 테이블 kimyongseon.member_group 구조 내보내기
CREATE TABLE IF NOT EXISTS `member_group` (
  `group_code` varchar(100) NOT NULL,
  `group_name` varchar(100) DEFAULT NULL,
  `group_des` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`group_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 테이블 데이터 kimyongseon.member_group:~2 rows (대략적) 내보내기
/*!40000 ALTER TABLE `member_group` DISABLE KEYS */;
INSERT IGNORE INTO `member_group` (`group_code`, `group_name`, `group_des`) VALUES
	('00', 'admin', 'admin..'),
	('01', 'group_01', 'group_01');
/*!40000 ALTER TABLE `member_group` ENABLE KEYS */;

-- 테이블 kimyongseon.test_recursive 구조 내보내기
CREATE TABLE IF NOT EXISTS `test_recursive` (
  `id` int(11) NOT NULL,
  `pid` int(11) DEFAULT NULL,
  `nm` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- 테이블 데이터 kimyongseon.test_recursive:~16 rows (대략적) 내보내기
/*!40000 ALTER TABLE `test_recursive` DISABLE KEYS */;
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
/*!40000 ALTER TABLE `test_recursive` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
####################################################################################################
####################################################################################################
--1 게시판 정렬
with recursive cte as
(
select  board_content_id,
        board_content_pid,
        member_id,
        board_content_title,
        board_content_body,
        board_content_regdatetime,
        board_content_edtdatetime,
        board_content_deleted,
        0 AS depth,
        CAST(LPAD(board_content_id, 10, "0") AS VARCHAR(1000)) as grp,
        CAST(LPAD(board_content_id, 10, "0") AS VARCHAR(1000)) as lvl
from    board
where   board_content_pid = -1 and board_id = :board_id
union all
select  r.board_content_id,
        r.board_content_pid,
        r.member_id,
        r.board_content_title,
        r.board_content_body,
        r.board_content_regdatetime,
        r.board_content_edtdatetime,
        r.board_content_deleted,
        depth + 1 AS depth,
        grp AS grp,
        CONCAT(cte.lvl, "-", LPAD(r.board_content_id, 10, "0")) as lvl
from    board r
inner join cte
        on r.board_content_pid = cte.board_content_id
)
SELECT * FROM
(SELECT * FROM
(SELECT @ROWNUM:=@ROWNUM+1 AS board_content_num, c.* 
FROM cte c, 
(SELECT @ROWNUM:=0) b ORDER BY CAST(board_content_id AS INTEGER)) t 
) a 
inner join member
on a.member_id = member.member_id
ORDER BY grp DESC, lvl
LIMIT :startrow, :numberInPage

--2. 댓글 정렬
with recursive cte as
(
select  comment_id,
        comment_pid,
        member_id,
        board_content_id,
        comment_body,
        comment_regdatetime,
        comment_edtdatetime,
        comment_deleted,
        0 AS depth,
        CAST(LPAD(comment_id, 10, "0") AS VARCHAR(1000)) as grp,
        CAST(LPAD(comment_id, 10, "0") AS VARCHAR(1000)) as lvl
from    comment
where   comment_pid = 0 and board_content_id = :board_content_id
union all
select  r.comment_id,
        r.comment_pid,
        r.member_id,
        r.board_content_id,
        r.comment_body,
        r.comment_regdatetime,
        r.comment_edtdatetime,
        r.comment_deleted,
        depth + 1 AS depth,
        grp AS grp,
        CONCAT(cte.lvl, "-", LPAD(r.comment_id, 10, "0")) as lvl
from    comment r
inner join cte
        on r.comment_pid = cte.comment_id
)
select * from cte
inner join member
on cte.member_id = member.member_id
ORDER BY lvl
####################################################################################################
####################################################################################################

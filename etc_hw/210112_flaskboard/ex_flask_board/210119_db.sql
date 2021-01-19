-- --------------------------------------------------------
-- 호스트:                          192.168.0.13
-- 서버 버전:                        10.5.5-MariaDB - mariadb.org binary distribution
-- 서버 OS:                        Win64
-- HeidiSQL 버전:                  11.0.0.5919
-- --------------------------------------------------------

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
  `board_content_id` varchar(100) NOT NULL,
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 테이블 데이터 kimyongseon.board:~38 rows (대략적) 내보내기
/*!40000 ALTER TABLE `board` DISABLE KEYS */;
INSERT IGNORE INTO `board` (`board_content_id`, `board_content_pid`, `member_id`, `board_id`, `board_content_title`, `board_content_body`, `board_content_regdatetime`, `board_content_edtdatetime`, `board_content_num`, `board_content_deleted`) VALUES
	('1', '0', 'abc', '05', '11', '11', '2021-01-18 12:05:21', '2021-01-18 12:05:21', '1', 'N'),
	('10', '0', 'abc', '02', '123', '123', '2021-01-18 12:39:01', '2021-01-18 12:39:01', '1', 'N'),
	('11', '0', 'abc', '02', '11', '11', '2021-01-18 12:49:16', '2021-01-18 12:49:16', '2', 'N'),
	('12', '0', 'abc', '01', '66', '66', '2021-01-18 16:17:47', '2021-01-18 16:17:47', '6', 'N'),
	('13', '0', 'abc', '01', 'aa', 'aa', '2021-01-18 16:17:52', '2021-01-18 16:17:52', '7', 'N'),
	('14', '0', 'abc', '01', 'ㅇㅇ', 'ㅇㅇ', '2021-01-18 16:18:06', '2021-01-18 16:18:06', '8', 'N'),
	('15', '0', 'abc', '01', '1', '1', '2021-01-18 16:18:11', '2021-01-18 16:18:11', '9', 'N'),
	('16', '0', 'abc', '01', 'ㅁㅁ', 'ㅁㅁ', '2021-01-18 16:18:18', '2021-01-18 16:18:18', '10', 'N'),
	('17', '0', 'abc', '01', '22', '22', '2021-01-18 16:18:22', '2021-01-18 16:18:22', '11', 'N'),
	('18', '0', 'abc', '01', 'ㄴㄴ', 'ㄴㄴ', '2021-01-18 16:18:28', '2021-01-18 16:18:28', '12', 'N'),
	('19', '12', 'abc', '01', 'ss', 'ss', '2021-01-18 20:45:01', '2021-01-18 20:45:03', '13', 'N'),
	('2', '0', 'abc', '05', '11', '11', '2021-01-18 12:22:18', '2021-01-18 12:22:18', '2', 'N'),
	('20', '19', 'abc', '01', 'ss', 'ss', '2021-01-18 20:46:56', '2021-01-18 20:46:56', '14', 'N'),
	('21', '20', 'abc', '01', 'ss', 'ss', '2021-01-18 20:47:10', '2021-01-18 20:47:10', '15', 'N'),
	('22', '19', 'abc', '01', 'ss', 'ss', '2021-01-18 20:47:39', '2021-01-18 20:47:39', '16', 'N'),
	('23', '0', 'abc', '01', 'dd', 'ee', '2021-01-18 22:03:22', '2021-01-18 22:03:22', '17', 'N'),
	('24', '0', 'abc', '01', '2101191225', 'dd', '2021-01-19 12:25:14', '2021-01-19 12:25:14', '18', 'N'),
	('25', '0', 'abc', '01', '2101191226', 'dd', '2021-01-19 12:25:22', '2021-01-19 12:25:22', '19', 'N'),
	('26', '0', 'abc', '01', 'aa', 'aa', '2021-01-19 12:25:27', '2021-01-19 12:25:27', '20', 'N'),
	('27', '0', 'abc', '01', 'bb', 'bb', '2021-01-19 12:25:31', '2021-01-19 12:25:31', '21', 'N'),
	('28', '0', 'abc', '01', 'cc', 'ccc', '2021-01-19 12:25:35', '2021-01-19 12:25:35', '22', 'N'),
	('29', '0', 'abc', '01', 'dd', 'dddd', '2021-01-19 12:25:38', '2021-01-19 12:25:38', '23', 'N'),
	('3', '0', 'abc', '05', '11', '11', '2021-01-18 12:24:51', '2021-01-18 12:24:51', '3', 'N'),
	('30', '0', 'abc', '01', 'ee', 'eeee', '2021-01-19 12:25:43', '2021-01-19 12:25:43', '24', 'N'),
	('31', '0', 'abc', '01', 'ttt', 'ccc', '2021-01-19 14:09:51', '2021-01-19 14:09:51', '25', 'N'),
	('32', '31', 'abc', '01', 'rettt', 'reccc', '2021-01-19 14:11:29', '2021-01-19 14:11:30', '26', NULL),
	('33', '31', 'abc', '01', 'rereaa', 'rerecc', '2021-01-19 14:41:46', '2021-01-19 14:41:46', '27', 'N'),
	('34', '33', 'abc', '01', 'rererecc', 'rererebb', '2021-01-19 14:42:03', '2021-01-19 14:42:03', '28', 'N'),
	('35', '34', 'abc', '01', 'rerereredd', 'rerererecc', '2021-01-19 14:42:23', '2021-01-19 14:42:23', '29', 'N'),
	('36', '33', 'abc', '01', 'rerereee', 'rererecc', '2021-01-19 14:42:38', '2021-01-19 14:42:38', '30', 'N'),
	('37', '35', 'abc', '01', 'rerererereff', 'reccc', '2021-01-19 14:43:08', '2021-01-19 14:43:08', '31', 'N'),
	('38', '36', 'abc', '01', 'rerereregg', 'rerereregg', '2021-01-19 14:43:29', '2021-01-19 14:43:29', '32', 'N'),
	('4', '0', 'abc', '05', '11', '11', '2021-01-18 12:25:38', '2021-01-18 12:25:38', '4', 'N'),
	('5', '0', 'abc', '01', '123', '1233', '2021-01-18 12:30:17', '2021-01-18 12:30:17', '1', 'N'),
	('6', '0', 'abc', '01', '123', '1233', '2021-01-18 12:36:47', '2021-01-18 12:36:47', '2', 'N'),
	('7', '0', 'abc', '01', '123', '1233', '2021-01-18 12:37:14', '2021-01-18 12:37:14', '3', 'N'),
	('8', '0', 'abc', '01', '123', '1233', '2021-01-18 12:37:18', '2021-01-18 12:37:18', '4', 'N'),
	('9', '0', 'abc', '01', '12333', '123', '2021-01-18 12:37:25', '2021-01-18 12:37:25', '5', 'N');
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
  `comment_id` int(11) NOT NULL DEFAULT 0,
  `comment_pid` varchar(100) DEFAULT NULL,
  `member_id` varchar(100) DEFAULT NULL,
  `board_content_id` varchar(100) DEFAULT NULL,
  `comment_body` varchar(1000) DEFAULT NULL,
  `comment_regdatetime` datetime DEFAULT NULL,
  `comment_edtdatetime` datetime DEFAULT NULL,
  `comment_deleted` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`comment_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 테이블 데이터 kimyongseon.comment:~5 rows (대략적) 내보내기
/*!40000 ALTER TABLE `comment` DISABLE KEYS */;
INSERT IGNORE INTO `comment` (`comment_id`, `comment_pid`, `member_id`, `board_content_id`, `comment_body`, `comment_regdatetime`, `comment_edtdatetime`, `comment_deleted`) VALUES
	(15, '0', 'abc', '29', 'abc', '2021-01-19 16:24:57', '2021-01-19 16:24:57', 'N'),
	(16, '0', 'abc', '29', 'abcee', '2021-01-19 16:25:06', '2021-01-19 16:25:06', 'N'),
	(17, '0', 'abc', '29', 'abceeff', '2021-01-19 16:25:09', '2021-01-19 16:25:09', 'N'),
	(18, '0', 'abc', '29', 'aaa', '2021-01-19 16:29:20', '2021-01-19 16:29:20', 'N'),
	(19, '16', 'abc', '29', 'abc', '2021-01-19 16:30:55', '2021-01-19 16:30:56', 'N');
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

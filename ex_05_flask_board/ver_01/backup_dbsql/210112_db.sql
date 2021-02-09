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

-- 테이블 데이터 kimyongseon.board:~0 rows (대략적) 내보내기
/*!40000 ALTER TABLE `board` DISABLE KEYS */;
/*!40000 ALTER TABLE `board` ENABLE KEYS */;

-- 테이블 kimyongseon.board_list 구조 내보내기
CREATE TABLE IF NOT EXISTS `board_list` (
  `board_id` varchar(100) NOT NULL,
  `board_name` varchar(100) DEFAULT NULL,
  `board_des` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`board_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 테이블 데이터 kimyongseon.board_list:~0 rows (대략적) 내보내기
/*!40000 ALTER TABLE `board_list` DISABLE KEYS */;
/*!40000 ALTER TABLE `board_list` ENABLE KEYS */;

-- 테이블 kimyongseon.comment 구조 내보내기
CREATE TABLE IF NOT EXISTS `comment` (
  `comment_id` varchar(100) NOT NULL,
  `comment_pid` varchar(100) DEFAULT NULL,
  `member_id` varchar(100) DEFAULT NULL,
  `board_content_id` varchar(100) DEFAULT NULL,
  `comment_body` varchar(1000) DEFAULT NULL,
  `comment_regdatetime` datetime DEFAULT NULL,
  `comment_edtdatetime` datetime DEFAULT NULL,
  `comment_deleted` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`comment_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

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

-- 테이블 데이터 kimyongseon.member:~0 rows (대략적) 내보내기
/*!40000 ALTER TABLE `member` DISABLE KEYS */;
/*!40000 ALTER TABLE `member` ENABLE KEYS */;

-- 테이블 kimyongseon.member_group 구조 내보내기
CREATE TABLE IF NOT EXISTS `member_group` (
  `group_code` varchar(100) NOT NULL,
  `group_name` varchar(100) DEFAULT NULL,
  `group_des` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`group_code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 테이블 데이터 kimyongseon.member_group:~0 rows (대략적) 내보내기
/*!40000 ALTER TABLE `member_group` DISABLE KEYS */;
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

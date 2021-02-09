-- --------------------------------------------------------
-- 호스트:                          192.168.0.13
-- 서버 버전:                        10.5.5-MariaDB - mariadb.org binary distribution
-- 서버 OS:                        Win64
-- HeidiSQL 버전:                  11.2.0.6213
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- kimyongseon 데이터베이스 구조 내보내기
CREATE DATABASE IF NOT EXISTS `kimyongseon` /*!40100 DEFAULT CHARACTER SET utf8 */;
USE `kimyongseon`;

-- 테이블 kimyongseon.alarm 구조 내보내기
CREATE TABLE IF NOT EXISTS `alarm` (
  `from_member_id` varchar(100) DEFAULT NULL,
  `to_member_id` varchar(100) DEFAULT NULL,
  `alarm_content` varchar(100) DEFAULT NULL,
  `alarm_regdatetime` varchar(100) DEFAULT NULL,
  `alarm_id` varchar(100) NOT NULL,
  `alarm_target_content_id` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`alarm_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- 테이블 데이터 kimyongseon.alarm:~1 rows (대략적) 내보내기
/*!40000 ALTER TABLE `alarm` DISABLE KEYS */;
INSERT INTO `alarm` (`from_member_id`, `to_member_id`, `alarm_content`, `alarm_regdatetime`, `alarm_id`, `alarm_target_content_id`) VALUES
	('admin', 'bcd', 'bb', '2021-02-05 16:28:54.925895', '5b88092a-3eb5-4d84-b84c-a36ed9aceba6', '85');
/*!40000 ALTER TABLE `alarm` ENABLE KEYS */;

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
) ENGINE=InnoDB AUTO_INCREMENT=86 DEFAULT CHARSET=utf8;

-- 테이블 데이터 kimyongseon.board:~85 rows (대략적) 내보내기
/*!40000 ALTER TABLE `board` DISABLE KEYS */;
INSERT INTO `board` (`board_content_id`, `board_content_pid`, `member_id`, `board_id`, `board_content_title`, `board_content_body`, `board_content_regdatetime`, `board_content_edtdatetime`, `board_content_num`, `board_content_deleted`) VALUES
	(1, '-1', 'abc', '01', 'aa', 'aa', '2021-01-20 15:31:29', '2021-01-20 15:31:29', NULL, 'N'),
	(2, '-1', 'abc', '01', 'bb', 'bb', '2021-01-20 15:51:50', '2021-01-20 15:51:50', NULL, 'Y'),
	(3, '2', 'abc', '01', 'rebb', 'bb', '2021-01-20 15:52:02', '2021-01-20 15:52:02', NULL, 'N'),
	(4, '3', 'abc', '01', 'rerebb', 'ree', '2021-01-20 15:54:44', '2021-01-20 15:54:44', NULL, 'N'),
	(5, '-1', 'abc', '01', 'cc', 'cc', '2021-01-20 15:59:23', '2021-01-20 15:59:23', NULL, 'Y'),
	(6, '2', 'abc', '01', 're2bbb', 'bbb', '2021-01-20 15:59:41', '2021-01-20 15:59:41', NULL, 'N'),
	(7, '-1', 'abc', '01', 'bbb', 'bbb', '2021-01-20 16:00:19', '2021-01-20 16:00:19', NULL, 'Y'),
	(8, '-1', 'abc', '02', 'dd', 'dd', '2021-01-20 16:00:26', '2021-01-20 16:00:26', NULL, 'N'),
	(9, '-1', 'abc', '01', 'ee', 'ee', '2021-01-20 16:00:32', '2021-01-20 16:00:32', NULL, 'N'),
	(10, '9', 'abc', '01', 'reaa', 're', '2021-01-20 16:00:42', '2021-01-20 16:00:42', NULL, 'Y'),
	(11, '-1', 'abc', '01', 'bb', 'bb', '2021-01-20 16:06:03', '2021-01-20 16:06:03', NULL, 'Y'),
	(12, '-1', 'abc', '01', 'ds', 'ds', '2021-01-20 16:06:08', '2021-01-20 16:06:08', NULL, 'Y'),
	(13, '10', 'abc', '01', '5시', 'ㅇ', '2021-01-20 17:01:39', '2021-01-20 17:01:39', NULL, 'N'),
	(14, '-1', 'bcd', '01', 'bcd', 'bcde', '2021-01-21 10:47:21', '2021-01-25 03:45:17', NULL, 'N'),
	(15, '-1', 'abc', '01', 'ee', 'ee', '2021-01-21 12:20:19', '2021-01-21 12:20:19', NULL, 'N'),
	(16, '-1', 'abc', '01', 'gg', 'gg', '2021-01-21 13:30:29', '2021-01-21 13:30:29', NULL, 'N'),
	(17, '-1', 'abc', '01', 'hh', 'hh', '2021-01-21 13:30:34', '2021-01-21 13:30:34', NULL, 'N'),
	(18, '-1', 'abc', '01', 'ii', 'iii', '2021-01-21 13:30:41', '2021-01-21 13:30:41', NULL, 'N'),
	(19, '-1', 'abc', '01', 'jj', 'jjjj', '2021-01-21 13:30:48', '2021-01-21 13:30:48', NULL, 'N'),
	(20, '-1', 'abc', '01', 'kk', 'kk', '2021-01-21 13:30:53', '2021-01-21 13:30:53', NULL, 'Y'),
	(21, '-1', 'abc', '01', 'kkㄷㄷ', 'kkㄷㄷ', '2021-01-21 14:38:57', '2021-01-21 14:38:57', NULL, 'Y'),
	(22, '-1', 'abc', '01', 'kkㄷㄷㄷ', 'kkㄷ', '2021-01-21 14:39:08', '2021-01-21 14:39:08', NULL, 'Y'),
	(23, '-1', 'abc', '01', 'kkㄷ', 'kkㄷㄷ', '2021-01-21 14:41:12', '2021-01-21 14:42:28', NULL, 'N'),
	(24, '-1', 'abc', '01', 'ee', 'eeggffff', '2021-01-22 13:16:25', '2021-01-25 03:41:02', NULL, 'N'),
	(25, '-1', 'admin', '02', 'bb', 'bb', '2021-01-22 14:50:56', '2021-01-22 14:50:56', NULL, 'N'),
	(26, '-1', 'admin', '01', 'aabb', 'aabbb', '2021-01-22 14:51:12', '2021-01-22 14:51:12', NULL, 'Y'),
	(27, '8', 'admin', '02', 'asdf', 'asdf', '2021-01-22 15:10:34', '2021-01-22 15:10:34', NULL, 'N'),
	(28, '-1', 'admin', '02', 'sdf', 'sd', '2021-01-22 15:58:51', '2021-01-22 15:58:51', NULL, 'N'),
	(29, '-1', 'admin', '02', '11', '11', '2021-01-22 16:01:40', '2021-01-22 16:01:40', NULL, 'N'),
	(30, '24', 'abc', '01', '0124', '11', '2021-01-24 23:51:00', '2021-01-24 23:51:00', NULL, 'N'),
	(31, '-1', 'admin', '02', '0125', 'ee', '2021-01-25 03:39:29', '2021-01-25 03:39:29', NULL, 'N'),
	(32, '-1', 'abc', '01', 'bbb', 'ccc', '2021-01-25 03:55:48', '2021-01-25 03:55:48', NULL, 'N'),
	(33, '32', 'abc', '01', 'ccc', 'ddd', '2021-01-25 03:55:56', '2021-01-25 03:55:56', NULL, 'N'),
	(34, '-1', 'abc', '01', 'cc', 'cc', '2021-01-25 11:54:08', '2021-01-25 11:54:08', NULL, 'N'),
	(35, '-1', 'abc', '04', 'aa', 'aa', '2021-01-25 11:54:27', '2021-01-25 11:54:27', NULL, 'N'),
	(36, '-1', 'abc', '05', 'bb', 'bb', '2021-01-25 11:54:40', '2021-01-25 11:54:40', NULL, 'N'),
	(37, '-1', 'abc', '01', 'bb', 'bb', '2021-01-25 12:18:11', '2021-01-25 12:18:11', NULL, 'N'),
	(38, '37', 'abc', '01', 'bbb', 'bbbbeeee', '2021-01-25 12:18:21', '2021-01-25 12:19:06', NULL, 'N'),
	(39, '37', 'abc', '01', 'ccdd', 'ccdd', '2021-01-25 12:19:19', '2021-01-25 12:19:19', NULL, 'Y'),
	(40, '-1', 'admin', '01', 'bb', 'bb', '2021-01-25 12:22:30', '2021-01-25 12:22:30', NULL, 'N'),
	(41, '-1', 'abc', '04', 'bb', 'bb', '2021-01-25 13:22:25', '2021-01-25 13:22:25', NULL, 'N'),
	(42, '-1', 'abc', '05', 'dd', 'dd', '2021-01-25 13:22:31', '2021-01-25 13:22:31', NULL, 'N'),
	(43, '-1', 'admin', '03', 'aa', 'aa', '2021-01-25 13:22:52', '2021-01-25 13:22:52', NULL, 'N'),
	(44, '-1', 'admin', '03', 'bb', 'bb', '2021-01-25 13:22:58', '2021-01-25 13:22:58', NULL, 'N'),
	(45, '-1', 'abc', '01', 'a', 'a', '2021-01-25 14:37:10', '2021-01-25 14:37:10', NULL, 'N'),
	(46, '30', 'abc', '01', 'ss', 'ss', '2021-01-25 15:07:18', '2021-01-25 15:07:18', NULL, 'N'),
	(47, '34', 'admin', '01', 'aa', 'aa', '2021-01-25 15:28:07', '2021-01-25 15:28:07', NULL, 'N'),
	(48, '47', 'admin', '01', 'bb', 'bb', '2021-01-25 15:28:17', '2021-01-25 15:28:17', NULL, 'N'),
	(49, '48', 'admin', '01', 'cc', 'cc', '2021-01-25 15:28:25', '2021-01-25 15:28:25', NULL, 'N'),
	(50, '-1', 'abc', '01', 'b', 'b', '2021-01-27 10:29:32', '2021-01-27 10:29:32', NULL, 'N'),
	(51, '-1', 'abc', '01', '55', '55', '2021-02-04 11:50:46', '2021-02-04 11:50:46', NULL, 'N'),
	(52, '45', 'abc', '01', '66', '66', '2021-02-04 11:50:58', '2021-02-04 11:50:58', NULL, 'N'),
	(53, '52', 'abc', '01', '77', '77', '2021-02-04 11:51:12', '2021-02-04 11:51:12', NULL, 'N'),
	(54, '51', 'abc', '01', '88', '88', '2021-02-04 11:51:20', '2021-02-04 11:51:20', NULL, 'N'),
	(55, '52', 'abc', '01', '99', '99', '2021-02-04 11:51:31', '2021-02-04 11:51:31', NULL, 'N'),
	(56, '45', 'abc', '01', '00', '00', '2021-02-04 11:51:41', '2021-02-04 11:51:41', NULL, 'N'),
	(57, '52', 'abc', '01', '11', '11', '2021-02-04 11:51:54', '2021-02-04 11:51:54', NULL, 'N'),
	(58, '31', 'admin', '02', 'ss', 'ss', '2021-02-04 11:54:31', '2021-02-04 11:54:31', NULL, 'N'),
	(59, '-1', 'admin', '01', '88', '88', '2021-02-04 11:54:38', '2021-02-04 11:54:38', NULL, 'N'),
	(60, '-1', 'admin', '02', 'ee', 'ee', '2021-02-04 11:54:49', '2021-02-04 11:54:49', NULL, 'N'),
	(61, '59', 'admin', '01', 'sdf', 'sdf', '2021-02-05 12:11:43', '2021-02-05 12:11:43', NULL, 'N'),
	(62, '59', 'admin', '01', 'sdf', 'sdf', '2021-02-05 12:23:31', '2021-02-05 12:23:31', NULL, 'N'),
	(63, '59', 'admin', '01', 'sdf', 'sdf', '2021-02-05 12:23:43', '2021-02-05 12:23:43', NULL, 'N'),
	(64, '59', 'admin', '01', 'sdf', 'sdf', '2021-02-05 12:23:59', '2021-02-05 12:23:59', NULL, 'N'),
	(65, '59', 'admin', '01', 'sdf', 'sdf', '2021-02-05 12:25:23', '2021-02-05 12:25:23', NULL, 'N'),
	(66, '-1', 'admin', '01', 'abc', 'abc', '2021-02-05 12:25:57', '2021-02-05 12:25:57', NULL, 'N'),
	(67, '-1', 'admin', '01', 'bbb', 'bb', '2021-02-05 12:26:47', '2021-02-05 12:26:47', NULL, 'N'),
	(68, '-1', 'admin', '01', 'cc', 'cc', '2021-02-05 12:27:32', '2021-02-05 12:27:32', NULL, 'N'),
	(69, '68', 'admin', '01', 'bb', 'bb', '2021-02-05 13:42:29', '2021-02-05 13:42:29', NULL, 'N'),
	(70, '-1', 'admin', '01', 'ff', 'ff', '2021-02-05 13:44:10', '2021-02-05 13:44:10', NULL, 'N'),
	(71, '-1', 'admin', '01', 'ff', 'ff', '2021-02-05 13:45:24', '2021-02-05 13:45:24', NULL, 'N'),
	(72, '38', 'admin', '01', 'cc', 'cc', '2021-02-05 13:49:03', '2021-02-05 13:49:03', NULL, 'N'),
	(73, '72', 'admin', '01', 'ee', 'ee', '2021-02-05 13:52:29', '2021-02-05 13:52:29', NULL, 'N'),
	(74, '73', 'admin', '01', 'gg', 'gg', '2021-02-05 13:52:55', '2021-02-05 13:52:55', NULL, 'N'),
	(75, '73', 'admin', '01', 'ff', 'ff', '2021-02-05 13:56:33', '2021-02-05 13:56:33', NULL, 'N'),
	(76, '74', 'admin', '01', 'ff', 'ff', '2021-02-05 13:57:07', '2021-02-05 13:57:07', NULL, 'N'),
	(77, '-1', 'bcd', '01', 'aa', 'aa', '2021-02-05 14:06:00', '2021-02-05 14:06:00', NULL, 'N'),
	(78, '77', 'abc', '01', 'bb', 'bb', '2021-02-05 14:16:58', '2021-02-05 14:16:58', NULL, 'N'),
	(79, '78', 'admin', '01', 'cc', 'cc', '2021-02-05 14:17:16', '2021-02-05 14:17:16', NULL, 'N'),
	(80, '77', 'admin', '01', 'dd', 'dd', '2021-02-05 14:17:25', '2021-02-05 14:17:25', NULL, 'N'),
	(81, '79', 'admin', '01', 'bb', 'bb', '2021-02-05 14:37:15', '2021-02-05 14:37:15', NULL, 'N'),
	(82, '79', 'admin', '01', '22', '22', '2021-02-05 14:38:13', '2021-02-05 14:38:13', NULL, 'N'),
	(83, '79', 'admin', '01', '22', '22', '2021-02-05 14:39:03', '2021-02-05 14:39:03', NULL, 'N'),
	(84, '79', 'admin', '01', 'ㄷㄷ', 'ㄷㄷ', '2021-02-05 14:41:12', '2021-02-05 14:41:12', NULL, 'N'),
	(85, '79', 'admin', '01', 'bb', 'bb', '2021-02-05 16:28:54', '2021-02-05 16:28:54', NULL, 'N');
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
INSERT INTO `board_list` (`board_id`, `board_name`, `board_des`) VALUES
	('01', 'board_01', 'board_01 설명...'),
	('02', 'board_02', 'board_02 설명..'),
	('03', 'board_03', 'board_03 설명...'),
	('04', 'board_04', 'board_04 설명.'),
	('05', 'board_05', 'board_05 설명..');
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
) ENGINE=InnoDB AUTO_INCREMENT=85 DEFAULT CHARSET=utf8;

-- 테이블 데이터 kimyongseon.comment:~40 rows (대략적) 내보내기
/*!40000 ALTER TABLE `comment` DISABLE KEYS */;
INSERT INTO `comment` (`comment_id`, `comment_pid`, `member_id`, `board_content_id`, `comment_body`, `comment_regdatetime`, `comment_edtdatetime`, `comment_deleted`) VALUES
	(45, '0', 'abc', '14', 'aa', '2021-01-21 11:30:19', '2021-01-21 11:30:19', 'N'),
	(46, '0', 'abc', '14', 'bb', '2021-01-21 11:30:22', '2021-01-21 11:30:22', 'N'),
	(47, '45', 'abc', '14', 'aa', '2021-01-21 11:30:26', '2021-01-21 11:30:26', 'N'),
	(48, '45', 'abc', '14', 'reaa', '2021-01-21 11:30:37', '2021-01-21 11:30:37', 'N'),
	(49, '47', 'abc', '14', 'rereaa', '2021-01-21 11:30:43', '2021-01-21 11:30:43', 'N'),
	(50, '48', 'abc', '14', 'rere2aa', '2021-01-21 12:03:53', '2021-01-21 12:03:53', 'N'),
	(51, '50', 'abc', '14', 'rerere2aa', '2021-01-21 12:03:58', '2021-01-21 12:03:58', 'N'),
	(52, '0', 'abc', '15', 'aa', '2021-01-21 12:20:26', '2021-01-21 12:20:26', 'N'),
	(53, '0', 'abc', '15', 'aabb', '2021-01-21 12:20:29', '2021-01-21 12:20:29', 'N'),
	(54, '0', 'abc', '20', 'aa', '2021-01-21 13:33:27', '2021-01-21 13:33:27', 'N'),
	(55, '0', 'abc', '20', 'aabb', '2021-01-21 13:36:40', '2021-01-21 13:36:40', 'Y'),
	(56, '0', 'abc', '20', 'reaa', '2021-01-21 13:36:45', '2021-01-21 13:36:45', 'Y'),
	(57, '54', 'abc', '20', '답aa', '2021-01-21 13:36:57', '2021-01-21 13:36:57', 'Y'),
	(58, '0', 'abc', '20', 'bb', '2021-01-21 14:02:05', '2021-01-21 14:02:05', 'Y'),
	(59, '0', 'abc', '20', 'cc', '2021-01-21 14:02:10', '2021-01-21 14:02:10', 'Y'),
	(60, '0', 'abc', '20', 'ccd', '2021-01-21 14:02:13', '2021-01-21 14:02:13', 'N'),
	(61, '57', 'abc', '20', 'bb', '2021-01-21 14:13:34', '2021-01-21 14:13:34', 'Y'),
	(62, '61', 'abc', '20', 'bbbb', '2021-01-21 14:13:38', '2021-01-21 14:13:38', 'N'),
	(63, '57', 'abc', '20', 'cc', '2021-01-21 14:13:47', '2021-01-21 14:13:47', 'N'),
	(64, '0', 'admin', '23', 'abc', '2021-01-22 13:06:38', '2021-01-22 13:06:38', 'N'),
	(65, '0', 'abc', '23', 'bbb', '2021-01-22 13:07:02', '2021-01-22 13:07:02', 'N'),
	(66, '0', 'abc', '23', 'cc', '2021-01-22 13:12:29', '2021-01-22 13:12:29', 'N'),
	(67, '0', 'abc', '23', 'dd', '2021-01-22 13:13:29', '2021-01-22 13:13:29', 'N'),
	(68, '0', 'admin', '8', 'dd', '2021-01-22 13:15:43', '2021-01-22 13:15:43', 'N'),
	(69, '0', 'abc', '24', 'dd', '2021-01-22 13:16:32', '2021-01-22 13:16:32', 'N'),
	(70, '0', 'abc', '8', 'aa', '2021-01-22 13:19:46', '2021-01-22 13:19:46', 'N'),
	(71, '70', 'abc', '8', 'aabb', '2021-01-22 13:19:56', '2021-01-22 13:19:56', 'N'),
	(72, '0', 'abc', '8', 'cd', '2021-01-22 13:40:25', '2021-01-22 13:40:25', 'N'),
	(73, '0', 'abc', '8', 'cd', '2021-01-22 13:40:25', '2021-01-22 13:40:25', 'N'),
	(74, '0', 'abc', '8', 'dd', '2021-01-22 13:41:51', '2021-01-22 13:41:51', 'N'),
	(75, '73', 'abc', '8', 'ddee', '2021-01-22 13:42:16', '2021-01-22 13:42:16', 'N'),
	(76, '0', 'abc', '24', 'ss', '2021-01-22 13:44:29', '2021-01-22 13:44:29', 'N'),
	(77, '0', 'admin', '8', 'ss', '2021-01-22 13:44:50', '2021-01-22 13:44:50', 'N'),
	(78, '0', 'bcd', '24', 'cde', '2021-01-22 14:18:25', '2021-01-22 14:18:25', 'Y'),
	(79, '0', 'admin', '24', 'abc', '2021-01-25 01:04:28', '2021-01-25 01:04:28', 'N'),
	(80, '0', 'abc', '32', 'ㄴㄴ', '2021-01-25 10:57:17', '2021-01-25 10:57:17', 'N'),
	(81, '0', 'abc', '36', 'aa', '2021-01-25 11:55:01', '2021-01-25 11:55:01', 'N'),
	(82, '0', 'abc', '37', 'cc', '2021-01-25 12:18:27', '2021-01-25 12:18:27', 'N'),
	(83, '0', 'abc', '45', 'aa', '2021-01-25 14:39:13', '2021-01-25 14:39:13', 'N'),
	(84, '0', 'abc', '42', 'aa', '2021-01-25 15:29:27', '2021-01-25 15:29:27', 'N');
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

-- 테이블 데이터 kimyongseon.group_authority:~2 rows (대략적) 내보내기
/*!40000 ALTER TABLE `group_authority` DISABLE KEYS */;
INSERT INTO `group_authority` (`group_code`, `authority_board_create`, `authority_board_update`, `authority_board_delete`) VALUES
	('00', '1', '1', '1'),
	('01', '0', '0', '0');
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

-- 테이블 데이터 kimyongseon.group_board_authority:~10 rows (대략적) 내보내기
/*!40000 ALTER TABLE `group_board_authority` DISABLE KEYS */;
INSERT INTO `group_board_authority` (`group_code`, `board_id`, `authority_board_content_read`, `authority_board_content_write`, `authority_board_content_update`, `authority_board_content_delete`) VALUES
	('00', '01', '2', '2', '2', '2'),
	('00', '02', '2', '2', '2', '2'),
	('01', '01', '1', '1', '1', '1'),
	('01', '02', '0', '0', '0', '0'),
	('00', '03', '2', '2', '2', '2'),
	('00', '04', '2', '2', '2', '2'),
	('00', '05', '2', '2', '2', '2'),
	('01', '03', '1', '0', '0', '0'),
	('01', '04', '1', '1', '0', '0'),
	('01', '05', '1', '1', '1', '0');
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

-- 테이블 데이터 kimyongseon.member:~9 rows (대략적) 내보내기
/*!40000 ALTER TABLE `member` DISABLE KEYS */;
INSERT INTO `member` (`member_id`, `group_code`, `member_pw`, `member_name`, `member_birthday`, `member_phonenumber`, `member_nickname`) VALUES
	('abc', '01', 'abc', 'abcname', '2021-01-12 00:00:00', '11', 'abcnname'),
	('admin', '00', 'admin', 'admin_name', '2021-01-15 13:18:22', '111111', 'admin_name'),
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
INSERT INTO `member_group` (`group_code`, `group_name`, `group_des`) VALUES
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
INSERT INTO `test_recursive` (`id`, `pid`, `nm`) VALUES
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
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;

# coding: utf-8
from sqlalchemy import Column, DateTime, String, Table
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Alarm(Base):
    __tablename__ = 'alarm'

    from_member_id = Column(String(100))
    to_member_id = Column(String(100))
    alarm_content = Column(String(100))
    alarm_regdatetime = Column(String(100))
    alarm_id = Column(String(100), primary_key=True)


class Board(Base):
    __tablename__ = 'board'

    board_content_id = Column(INTEGER(11), primary_key=True)
    board_content_pid = Column(String(100))
    member_id = Column(String(100))
    board_id = Column(String(100))
    board_content_title = Column(String(100))
    board_content_body = Column(String(1000))
    board_content_regdatetime = Column(DateTime)
    board_content_edtdatetime = Column(DateTime)
    board_content_num = Column(String(100))
    board_content_deleted = Column(String(10))


class BoardList(Base):
    __tablename__ = 'board_list'

    board_id = Column(String(100), primary_key=True)
    board_name = Column(String(100))
    board_des = Column(String(1000))


class Comment(Base):
    __tablename__ = 'comment'

    comment_id = Column(INTEGER(11), primary_key=True)
    comment_pid = Column(String(100))
    member_id = Column(String(100))
    board_content_id = Column(String(100))
    comment_body = Column(String(1000))
    comment_regdatetime = Column(DateTime)
    comment_edtdatetime = Column(DateTime)
    comment_deleted = Column(String(10))


class File(Base):
    __tablename__ = 'file'

    file_id = Column(String(100), primary_key=True)
    board_content_id = Column(String(100))
    member_id = Column(String(100))
    file_name = Column(String(100))
    file_path = Column(String(100))
    file_type = Column(String(100))
    file_regdatetime = Column(DateTime)
    file_edtdatetime = Column(DateTime)


class GroupAuthority(Base):
    __tablename__ = 'group_authority'

    group_code = Column(String(100), primary_key=True)
    authority_board_create = Column(String(10))
    authority_board_update = Column(String(10))
    authority_board_delete = Column(String(10))


t_group_board_authority = Table(
    'group_board_authority', metadata,
    Column('group_code', String(100)),
    Column('board_id', String(100)),
    Column('authority_board_content_read', String(10)),
    Column('authority_board_content_write', String(10)),
    Column('authority_board_content_update', String(10)),
    Column('authority_board_content_delete', String(10))
)


class Member(Base):
    __tablename__ = 'member'

    member_id = Column(String(100), primary_key=True)
    group_code = Column(String(100))
    member_pw = Column(String(100))
    member_name = Column(String(100))
    member_birthday = Column(DateTime)
    member_phonenumber = Column(String(100))
    member_nickname = Column(String(100))


class MemberGroup(Base):
    __tablename__ = 'member_group'

    group_code = Column(String(100), primary_key=True)
    group_name = Column(String(100))
    group_des = Column(String(1000))


class TestRecursive(Base):
    __tablename__ = 'test_recursive'

    id = Column(INTEGER(11), primary_key=True)
    pid = Column(INTEGER(11))
    nm = Column(String(20))

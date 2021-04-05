# coding: utf-8
from sqlalchemy import Column, DateTime, String, Table
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base

# print('dto >> model.py')

Base = declarative_base()
metadata = Base.metadata

class Member(Base):
    __tablename__ = 'member'

    member_id = Column(String(100), primary_key=True)
    group_code = Column(String(100))
    member_pw = Column(String(100))
    member_name = Column(String(100))
    member_birthday = Column(DateTime)
    member_phonenumber = Column(String(100))
    member_nickname = Column(String(100))

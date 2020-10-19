import string, random, time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, VARCHAR, NUMERIC, CHAR, DATETIME, TEXT
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://{username}:{password}@{hostname}:{port}/{databasename}".format(
    username="scott",
    password="tiger",
    hostname="192.168.56.1",
    port="3306",
    databasename="test"
)

#데이터 베이스에 접속한다.
DATABASES = create_engine(SQLALCHEMY_DATABASE_URI, echo = True)
Base = declarative_base()

# Database를 없으면 생성
Base.metadata.create_all(DATABASES)

# 세션을 만들어서 연결시킨다.

Session = sessionmaker()
Session.configure(bind=DATABASES)
session = Session()

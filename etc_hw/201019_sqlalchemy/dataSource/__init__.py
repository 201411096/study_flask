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

def insertData(data):
    session.add(data)
    session.commit()

def insertAllData(datas):
    for data in datas:
        session.add(data)
    session.commit()

def selectData(data, **kwargs):
    keyList = kwargs.keys()
    result = session.query(data)    
    
    if('where' in keyList):
        result = result.filter(text(kwargs['where']))
    if('withEntities' in keyList):
        result = result.with_entities(*(kwargs['withEntities'])) # kwargs['withEntities]의 값이 list로 넘어오고 리스트로 넘어온 값을 unpacking해서 with_entities()의 매개변수로 넣어줌
    if('groupBy' in keyList):
        result = result.group_by(*(kwargs['groupBy']))
    if('having' in keyList):
        result = result.having(text(kwargs['having']))
    if('orderBy' in keyList):
        result = result.order_by(text(kwargs['orderBy']))

    if('type' in keyList):
        if(kwargs['type']=='query'):
            return result
        elif(kwargs['type']=='subquery'):
            return result.subquery()
        elif(kwargs['type']=='one'):
            return result.one()
        else:
            return result.all()
    else:
        return result.all()

def deleteData(data, **kwargs):
    keyList = kwargs.keys()
    targetData = session.query(data)
    deleteCnt = 0
    if('where' in keyList):
        targetData = targetData.filter(text(kwargs['where']))

    for row in targetData:
        session.delete(row)
        deleteCnt+=1
    session.commit()
    return deleteCnt

def updateData(data, dataContent, **kwargs):
    keyList = kwargs.keys()
    dataContentKeyList = dataContent.keys()
    targetData = session.query(data)
    updateCnt = 0
    if('where' in keyList):
        targetData = targetData.filter(text(kwargs['where']))

    for row in targetData:
        for dataContentKey in dataContentKeyList:
            setattr(row, dataContentKey, dataContent[dataContentKey])
        updateCnt+=1
    session.commit()
    return updateCnt
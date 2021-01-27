from flask import render_template, request, redirect
from flask import session as flaskSession
from functools import wraps
import datetime

def queryToDict(statement):
    result = []
    rows = statement.all()

    for row in rows:
        result.append(row._asdict())
    return result

def queryToDict2(data):
    return [{column: value for column, value in rowproxy.items()} for rowproxy in data]

def authDecorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if(flaskSession.get('userData') is None):
            return redirect('/render/login')
        return func(*args, **kwargs)
    return wrapper


##### test #####
from sqlalchemy import exc

def convertStatementToList(statement):
    result = {}
    dataList = []
    rows = statement.all()

    for row in rows:
        dataList.append(row._asdict())
    result['data'] = dataList
    return result

# sql 직접 사용시에..
def convertStatementToList2(data):
    result = {}
    dataList = [{column: value for column, value in rowproxy.items()} for rowproxy in data]
    result['data'] = dataList
    return result

def sessionAdd(dataObject, session):
    result = {}
    try:
        session.add(dataObject)
        session.commit()
        result['code'] = '1'
    except exc.IntegrityError as e:
        print(e)
        session.rollback()
        result['code'] = '0'
    return result

def returnCodeAfterUpdate(resultCount):
    result = {}
    if resultCount>=1:
        result['code']='1'
    else:
        result['code']='0'
    return result
##### test #####
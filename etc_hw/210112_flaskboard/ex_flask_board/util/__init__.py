from flask import render_template, request, redirect
from flask import session as flaskSession
from functools import wraps

def queryToDict(statement):
    # print('statement(queryToDict) : ', statement)
    # print('statement.all() (queryToDict) : ', statement.all())
    result = []
    rows = statement.all()

    for row in rows:
        # print('row(queryToDict) : ', row)
        # print('type of row(queryToDict) : ', type(row))
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

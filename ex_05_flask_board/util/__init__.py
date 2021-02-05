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

from flask import render_template, request
from flask import session as flaskSession

def queryToDict(statement):
    result = []
    rows = statement.all()

    for row in rows:
        result.append(row._asdict())
    return result

def authDecorator(func):
    def wrapper(*args, **kwargs):
        print('before innerFunc ...')
        if(flaskSession.get('userData') is not None):
            return render_template('login.html')
        func(*args, **kwargs)
        print('after innerFunc ...')
    return wrapper

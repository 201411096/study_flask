from flask import Flask, Response, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func, distinct, case, between
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
import datetime
import json
import pandas as pd
from sqlalchemy.dialects.mysql import \
        BIGINT, BINARY, BIT, BLOB, BOOLEAN, CHAR, DATE, \
        DATETIME, DECIMAL, DECIMAL, DOUBLE, ENUM, FLOAT, INTEGER, \
        LONGBLOB, LONGTEXT, MEDIUMBLOB, MEDIUMINT, MEDIUMTEXT, NCHAR, \
        NUMERIC, NVARCHAR, REAL, SET, SMALLINT, TEXT, TIME, TIMESTAMP, \
        TINYBLOB, TINYINT, TINYTEXT, VARBINARY, VARCHAR, YEAR


app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:sm1418!1662@192.168.0.13:3306/test'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://scott:tiger@192.168.56.1:3306/test'

# SQLALCHEMY_TRACK_MODIFICATIONS : 옵션을 추가하지 않으면 FSADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS 경고메시지 발생
# ['SQLALCHEMY_TRACK_MODIFICATIONS'] = True -> sqlalchemy가 객체 수정을 추적하고 신호를 보냄 (추가적인 메모리를 사용)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)
CORS(app)

# 샘플데이터1 구조
class emp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    gender = db.Column(db.String(16))
    age = db.Column(db.Integer)
    location = db.Column(db.Integer)
    deptno = db.Column(db.Integer)
    hiredate = db.Column(db.DateTime, default=datetime.datetime.utcnow())
    salary = db.Column(db.Integer)

# 샘플데이터2 구조
class board(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    writer_id = db.Column(db.String(64))
    title = db.Column(db.String(128))
    content = db.Column(LONGTEXT)

def checkQueryInConsole(orm_result, caseOption):
    print('-------------------------------------------------------------')
    print('Query : ' + caseOption)
    print(orm_result)
    print('-------------------------------------------------------------')

def test_raw_sql():
    lines = ''
    myfile = open("./ex_03_SQLAlchemy/test/test_file/sample.txt")
    lines = myfile.read()
    myfile.close()
    board_content=lines
    print('lines : ' + board_content)
    arg_sql_query ="INSERT INTO board(id, writer_id, title, content) VALUES (23, 'abc1237', 'title23',"+ board_content +")"

    results = db.session.execute(arg_sql_query)
    db.session.commit()
    print('result : ' + results)

    return Response(
        response = json.dumps({'test':'testtt'}),
        status = 200,
        mimetype="application/json"
    )


if __name__ == '__main__':
    print('11')
    test_raw_sql()



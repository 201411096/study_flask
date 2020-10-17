from flask import Flask, Response, request, jsonify
from flask_cors import CORS
import json
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func, distinct, case, between
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound
import pandas as pd
from sqlalchemy.dialects.mysql import \
        BIGINT, BINARY, BIT, BLOB, BOOLEAN, CHAR, DATE, \
        DATETIME, DECIMAL, DECIMAL, DOUBLE, ENUM, FLOAT, INTEGER, \
        LONGBLOB, LONGTEXT, MEDIUMBLOB, MEDIUMINT, MEDIUMTEXT, NCHAR, \
        NUMERIC, NVARCHAR, REAL, SET, SMALLINT, TEXT, TIME, TIMESTAMP, \
        TINYBLOB, TINYINT, TINYTEXT, VARBINARY, VARCHAR, YEAR

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:sm1418!1662@192.168.0.13:3306/fems'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://scott:tiger@192.168.56.1:3306/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)


@app.route('/dataFromDb')
def sendData():
    arg_sql_query = request.args.get('query')

    results = db.session.execute('SHOW TABLES FROM fems')

    result = []
    for row in results:
        print(row['Tables_in_fems'])
        tempRow = str(row['Tables_in_fems'])
        result.append(tempRow)
    print('----- end table list -----')
    tableLength = len(result)
    changedCnt = 0
    exceptionCnt = 0
    for resultRow in result:
        rowQuery = 'ALTER TABLE ' + resultRow + arg_sql_query
        try:
            db.session.execute(rowQuery)
            print('changed table : ' + resultRow)
            changedCnt +=1
        except:
            print('exception table : ' + resultRow)
            exceptionCnt+=1

    print('변화된 테이블 개수 : ', changedCnt)
    print('예외처리된 테이블 개수 : ', exceptionCnt)
    print('총 테이블 개수 : ', tableLength)
    return Response(
        response = json.dumps(result), # dict -> json
        status = 200,
        mimetype="application/json"
    )

if __name__ == '__main__':
    app.run(host="192.168.0.51", port="5000")
    # app.run(host="192.168.56.1", port="5000")
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
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://scott:tiger@192.168.56.1:3306/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)

@app.route('/dataFromServer')
def sendSampleData():
    with open('yourFile.txt') as MyFile:
        fileData = MyFile.read()
        print(fileData)
        fileData = json.loads(fileData)
        return Response(
            response = json.dumps(fileData),
            status = 200,
            mimetype="application/json"
        )

@app.route('/dataFromDb')
def sendData():
    arg_sql_query = request.args.get('query')

    results = db.session.execute(arg_sql_query)

    result = []
    for row in results:
        result.append(dict(row))

    return Response(
        response = json.dumps(result), # dict -> json
        status = 200,
        mimetype="application/json"
    )

if __name__ == '__main__':
    # app.run(host="192.168.0.51", port="5000")
    app.run(host="192.168.56.1", port="5000")
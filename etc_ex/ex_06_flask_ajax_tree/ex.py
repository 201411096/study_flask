from flask import Flask, render_template, Response, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
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
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:sm1418!1662@192.168.0.13:3306/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)
app.debug = True

class tree_table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pid = db.Column(db.Integer)
    name = db.Column(db.String(20))
    description = db.Column(db.String(500))

@app.route('/test')
def test():
    return render_template('application.html')

@app.route('/raw_sql')
def raw_sql():
    raw_sql = request.args.get('query')
    results = db.session.execute(raw_sql)

    result = []
    for row in results:
        result.append(dict(row))

    return Response(
        response = json.dumps(result),
        status = 200,
        mimetype = "application/json"
    )

@app.route('/raw_sql_iud')
def raw_sql_02():
    raw_sql = request.args.get('query')
    result = db.session.execute(raw_sql)
    db.session.commit()
    result = {'result':'result'}
    return Response(
        response = json.dumps(result),
        status = 200,
        mimetype = "application/json"
    )

if __name__ == '__main__':
     app.run(host="192.168.0.51", port="5000")


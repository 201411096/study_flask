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

class board(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    writer_id = db.Column(db.String(64))
    title = db.Column(db.String(128))
    content = db.Column(LONGTEXT)

@app.route('/test')
def test():
    return render_template('application.html')

@app.route('/test_ajax')
def test_ajax():
    test_sql = 'select * from board'
    results = db.session.execute(test_sql)

    result = []
    for row in results:
        result.append(dict(row))

    return Response(
        response = json.dumps(result),
        status = 200,
        mimetype = "application/json"
    )

if __name__ == '__main__':
     app.run(host="192.168.0.51", port="5000")


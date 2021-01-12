from flask import Flask, Response, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
__all__ = ['app']

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:sm1418!1662@192.168.0.13:3306/test'

db = SQLAlchemy(app)
CORS(app)

from services import *


@app.route('/test_bbb')
def bbb():
    return 'bbb'

if __name__ == '__main__':
    app.run(debug=True)
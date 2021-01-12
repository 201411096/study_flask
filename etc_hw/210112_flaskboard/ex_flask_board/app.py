from flask import Flask, Response, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
__all__ = ['app', 'session', 'Base']

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

CORS(app)

from database import Base, session
from services import *


@app.route('/test_bbb')
def bbb():
    return 'bbb'

if __name__ == '__main__':
    app.run(debug=True)
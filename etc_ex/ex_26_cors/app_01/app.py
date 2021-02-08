from flask import Flask, Response, request, jsonify, render_template
from flask_cors import CORS, cross_origin

appHost = '192.168.0.51'
appPort = '5000'

app = Flask(__name__)

# CORS(app, resources={r"/": {"origins": "*"}})

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = '111'

@app.route('/a')
@cross_origin()
def test_a():
    return {"a":"aa"}

@app.route('/b')
def test_b():
    return {"b":"bb"}

@app.route('/c')
@cross_origin(origins='http://192.168.0.51:3000')
def test_c():
    return {"c":"cc"}

if __name__ == '__main__':
    app.run(host=appHost, port=appPort, debug=True)
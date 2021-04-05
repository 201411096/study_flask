from flask import Flask, Response, request, jsonify, render_template
from flask_cors import CORS, cross_origin

appHost = '192.168.0.51'
appPort = '3000'

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = '111'

@app.route('/')
def test_render():
    return render_template('test.html')

if __name__ == '__main__':
    app.run(host=appHost, port=appPort, debug=True)
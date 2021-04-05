from flask import Flask, Response, render_template, request
from flask_sse import sse
from flask_cors import CORS
import redis

app = Flask(__name__)
CORS(app)
app.config["REDIS_URL"]="redis://localhost:6379"
app.register_blueprint(sse, url_prefix='/stream')
appRedis = redis.StrictRedis(host='localhost', port=6379, db=0) # redis default port : 6379

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/sample')
def render_template_sample():
    return render_template('client.html')

@app.route('/send')
def send_message():
    sse.publish({"message": "Hello!"}, type='greeting')
    return "Message sent!"

@app.route('/test_redis', methods=["POST"])
def redis_set():
    datas = request.get_json()
    for key in datas.keys():
        appRedis.set(key, datas[key])
    return 'redis set...'
    
@app.route('/test_redis/<key>', methods=["GET"])
def redis_get(key):
    result = {}
    if appRedis.get(key) is not None:
        result[key] = appRedis.get(key)
    return result

@app.route('/test_redis/<key>', methods=["DELETE"])
def redis_delete(key):
    appRedis.delete(key)
    return 'redis delete...'

@app.route('/test_redis/deleteAll', methods=["DELETE"])
def redis_deleteAll():
    appRedis.flushdb()
    return 'redis deleteAll..'

if __name__ == '__main__':
     app.run(host="127.0.0.1", port="5000")

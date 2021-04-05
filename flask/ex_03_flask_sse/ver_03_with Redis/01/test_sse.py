from flask import Flask, Response, render_template, request, session, escape
from flask_cors import CORS
import redis
import json
import uuid

app = Flask(__name__)
CORS(app)
appRedis = redis.StrictRedis(host='localhost', port=6379, db=0) # redis default port : 6379
app.config['SECRET_KEY']='aaaa'

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/sample')
def render_template_sample():
    return render_template('client.html')

def event_stream():
    pub = appRedis.pubsub() # Publish/Subscribe object (you can subscribe to channels and listen for messages)
    pub.subscribe('sse_example_channel')
    for msg in pub.listen():
        print('check msg in event_stream() ...', msg)
        print('msg type ...', type(msg['channel'])) # bytes
        
        if msg['type'] == 'pmessage':
            event, data = json.loads(msg['data'])
            yield u'event: {0}\ndata: {1}\n\n'.format(event, data)
        else:
            yield u'data: {0}\n\n'.format(msg['data'])

@app.route('/stream', methods=['GET'])
def get_pushes():
    session['abcabc']=uuid.uuid4()
    print('========== clientList check ==========')
    print(appRedis.client_list())
    print('clientList Length : ', len(appRedis.client_list()))
    print('========== clientList check ==========')
    print('event stream result :', event_stream())      # <generator object event_stream at 0x00000185334B85C8>
    print('event stream type :', type(event_stream()))  # <class 'generator'>
    return Response(event_stream(), mimetype="text/event-stream")   # 응답의 형식 : event-stream

@app.route('/post')
def publish_data():
    appRedis.publish('sse_example_channel', json.dumps({'data':'bb', 'b':'cc'}))
    return 'publish_data ...'

@app.route('/post2')
def publish_data2():
    appRedis.publish('sse_example_channel2', json.dumps({'data':'aa', 'b':'bb'}))
    return 'publish_data ...'

if __name__ == '__main__':
    app.run(host="192.168.0.51", port="5000")
    # app.run(host="127.0.0.1", port="5000")
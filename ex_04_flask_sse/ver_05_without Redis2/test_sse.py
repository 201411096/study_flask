from flask import Flask, Response, render_template, request, session, escape
from flask_cors import CORS
import redis
import json
import uuid
import time
app = Flask(__name__)
CORS(app)
appRedis = redis.StrictRedis(host='localhost', port=6379, db=0) # redis default port : 6379
app.config['SECRET_KEY']='aaaa'

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/sample')
def render_template_sample():
    return render_template('client1.html')

def event_stream():
    try:
        pubsub = appRedis.pubsub()
        pubsub.subscribe('chat')
        #for message in pubsub.listen():#This doesn't work because it's blocking
        while True:
            message = pubsub.get_message()

            if not message:
                # The yield is necessary for this to work!
                # In my case I always send JSON encoded data
                # An empty response might work, too.
                yield "data: {}\n\n"
                time.sleep(0.1)
                continue
                # -> 0.1초마다 비어있는 json 전송
                
            # If the nonblocking get_message() returned something, proceed normally
            yield 'data: %s\n\n' % message["data"]
            
    finally:
        print("CLOSED!")
        # Your closing logic here (e.g. marking the user as offline in your database)

@app.route('/stream', methods=['GET'])
def get_pushes():
    # print('========== clientList check ==========')
    print(appRedis.client_list())
    print('clientList Length : ', len(appRedis.client_list()))
    # print('========== clientList check ==========')
    return Response(event_stream(), mimetype="text/event-stream")

@app.route('/post')
def publish_data():
    appRedis.publish('sse_example_channel', json.dumps({'data':'bb', 'b':'cc'}))
    return 'publish_data ...'

@app.route('/post2')
def publish_data2():
    appRedis.publish('sse_example_channel2', json.dumps({'data':'aa', 'b':'bb'}))
    return 'publish_data ...'

if __name__ == '__main__':
    app.run(host="192.168.0.51", port="5000", debug=True)
    # app.run(host="127.0.0.1", port="5000")
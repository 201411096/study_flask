from flask import Flask, Response, render_template, request, session, escape
from flask_cors import CORS
import redis
import json
import time

# reference
# https://stackoverflow.com/questions/18383008/python-flask-how-to-detect-a-sse-client-disconnect-from-front-end-javascript
# https://stackoverflow.com/questions/18383008/python-flask-how-to-detect-a-sse-client-disconnect-from-front-end-javascript/56188220#56188220
# https://stackoverrun.com/ko/q/5012145

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
        pubsub.subscribe('sse_example_channel')
        #for message in pubsub.listen():#This doesn't work because it's blocking
        while True:
            message = pubsub.get_message()  # pubsub기 존재하지 않을 경우 예외가 발생하면서 pubsub 객체를 reset하는 방식
            if not message:
                # The yield is necessary for this to work!
                # In my case I always send JSON encoded data
                # An empty response might work, too.
                yield "data: {}\n\n"
                time.sleep(1)
                continue

            # If the nonblocking get_message() returned something, proceed normally
            yield 'data: %s\n\n' % message["data"]
    except GeneratorExit:
        print('generatorExit...')
    finally:
        # Your closing logic here (e.g. marking the user as offline in your database)
        pubsub.reset()
        # print('check clientNumber(event_stream .. finally) : ', len(appRedis.client_list())) # 아래 코드 활성화시 정상 작동 안됨
        

@app.route('/stream', methods=['GET'])
def get_pushes():
    print('check clientNumber(get_pushes ..) : ', len(appRedis.client_list()))
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
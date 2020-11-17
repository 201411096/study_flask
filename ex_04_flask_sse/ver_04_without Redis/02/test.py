from flask import Flask, Response, render_template, request, session, escape
from flask_cors import CORS
import json
import time
import queue
import uuid
app = Flask(__name__)
CORS(app)

clientList = []
appQueue = queue.Queue(maxsize=5)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/sample')
def render_template_sample():
    return render_template('client.html')

@app.route('/stream')
def stream():
    def event_stream():
        clientId = uuid.uuid4()
        clientList.append(clientId)
        print('0. checkPoint before try statement => length of clientList : ', len(clientList))
        try:
            messages = appQueue
            while True:
                try:
                    print('1. checkPoint in try statement')
                    msg = messages.get_nowait()
                except Exception:
                    print('2. checkPoint in except statement')
                    msg = None
                print('2_5. checkPoint after except statement => msg :', msg)
                print('2_7. checkPoint after except statement => not msg :', not msg)
                if not msg:
                    print('3. checkPoint in if statement')
                    yield 'data: {}\n\n'
                    time.sleep(3)
                    continue
                print('3_5. checkPoint after if statement => dataFormat : ', 'data: {0}\n\n'.format(msg))
                yield 'data: {0}\n\n'.format(msg)
                print('3_6. checkPoint after yield statement ...')
        except GeneratorExit:
            print('generatorExit ...')
            print('4. checkPoint in except generatorExit statement')
        finally:
            print('5. checkPoint in finally statement')
            print('close ...')
            clientList.remove(clientId)
    return Response(event_stream(), mimetype='text/event-stream')

@app.route('/post', methods=['post'])
def postData():
    requestBody = request.get_json()
    requestBody = {'a':'aa', 'b':'bb'}
    appQueue.put_nowait(requestBody)
    return 'post...'

if __name__ == '__main__':
    app.run(host="192.168.0.51", port="5000", debug=True)
    # app.run(host="127.0.0.1", port="5000")
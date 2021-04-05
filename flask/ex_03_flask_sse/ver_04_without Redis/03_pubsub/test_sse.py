# issue
# 같은 id에 다른 uuid 일 경우 messageQueue 문제 발생

from flask import Flask, Response, render_template, request, session, escape
from flask_cors import CORS
import json
import time
import queue
import uuid
import traceback

app = Flask(__name__)
CORS(app)

# clientList = []
# appQueue = queue.Queue(maxsize=5)

class PubSub:
    def __init__(self):
        self.listeners = {}
    
    def getListener(self, id, uniqueId):
        if id not in self.listeners:
            self.listeners[id] = {}
            self.listeners[id]['channel'] = set()  # channelSet
            q = queue.Queue(maxsize=10)
            self.listeners[id]['messageQueue'] = q
            self.listeners[id]['uniqueIdSet'] = set()
        self.listeners[id]['uniqueIdSet'].add(uniqueId)
        return self.listeners[id]

    def closeListener(self, id, uniqueId):
        try:
            self.listeners[id]['uniqueIdSet'].remove(uniqueId)
            if len(self.listeners[id]['uniqueIdSet']) == 0 :
                self.removeListener(id)
        except:
            print('except in closeListener ... ')
    
    def removeListener(self, id):
        del self.listeners[id]

    def publish(self, **kwargs):
        for id in self.listeners:
            channel = kwargs.get('channel', 'system_channel')
            message = kwargs.get('message', '')
            try:
                if channel == 'system_channel':
                    self.listeners[id]['messageQueue'].put_nowait(message)
                elif channel in self.listeners[id]['channel']:
                    self.listeners[id]['messageQueue'].put_nowait(message)
            except queue.Full:
                print('queue.Full Exception ...')

    def subscribe(self, id, channel):
        self.listeners[id]['channel'].add(channel)

    def unsubscribe(self, id, channel):
        try:
            self.listeners[id]['channel'].remove(channel)
        except KeyError:
            print('unsubscribe keyError ...')

pubSub = PubSub()

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/sample')
def render_template_sample():
    return render_template('client.html')

@app.route('/stream/<clientId>')
def stream(clientId):
    def event_stream():
        uniqueId = uuid.uuid4()
        # clientId = uuid.uuid4()
        # clientList.append(clientId)
        myListener = pubSub.getListener(clientId, uniqueId)
        print('0. checkPoint before try statement => length of clientList : ', len(pubSub.listeners))
        try:
            messages = myListener['messageQueue']
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
            # clientList.remove(clientId)
            pubSub.closeListener(clientId, uniqueId)
    return Response(event_stream(), mimetype='text/event-stream')

@app.route('/pubsub', methods=["POST"])
def doPubsub():
    """
    requestBody = {
        "id":"target_client_id ...",
        "channel":"target_channel ...",
        "subscribe_flag" : "subscribe or unsubscribe"
    }
    """
    requestBody = request.get_json()
    if(requestBody['subscribe_flag'] == 'subscribe'):
        pubSub.subscribe(requestBody["id"], requestBody["channel"])
    elif(requestBody['subscribe_flag'] == 'unsubscribe'):
        pubSub.unsubscribe(requestBody["id"], requestBody["channel"])
    return 'doPubsub ...'
    

@app.route('/post', methods=['post'])
def postData():
    """
    requestBody = {
        "channel" : "target_channel ...",
        "data" : "your_data_content ..."
    }
    """
    requestBody = request.get_json()
    # requestBody = {}
    # requestBody['data'] = {'a':'aa', 'b':'bb'}
    # appQueue.put_nowait(requestBody)
    if requestBody.get('channel', None) is not None:
        pubSub.publish(channel=requestBody['channel'], message=json.dumps(requestBody['data']))
    else:
        pubSub.publish(message=json.dumps(requestBody['data']))
    return 'post...'

if __name__ == '__main__':
    app.run(host="192.168.0.51", port="5000", debug=True)
    # app.run(host="127.0.0.1", port="5000")
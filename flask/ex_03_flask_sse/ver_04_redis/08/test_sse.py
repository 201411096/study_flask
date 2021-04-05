from flask import Flask, Response, render_template, request, session, escape
from flask_cors import CORS
import redis
import json

app = Flask(__name__)
CORS(app)
appRedis = redis.StrictRedis(host='192.168.0.51', port=6379, db=0, charset="utf-8", decode_responses=True) # redis default port : 6379
app.config['SECRET_KEY']='aaaa'

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/sample')
def render_template_sample():
    return render_template('client.html')

@app.route('/stream/<id>', methods=['GET'])
def get_pushes(id):
    clientId = id

    def subscribeProcess(messageDict, pubsub):
        print('check messageDict in subscribeProcess', messageDict)
        print('check pubsub.id in subscribeProcess', pubsub.id)
        if messageDict.get("id", None) != str(pubsub.id):
            return 0
        else:
            if messageDict["subscribe_flag"] == "subscribe":
                print(pubsub.id , "is now subscribing to ", messageDict['channel'])
                pubsub.subscribe(messageDict["channel"])
                return 1
            elif messageDict["subscribe_flag"] == "unsubscribe":
                print(pubsub.id , "is now unsubscribing to ", messageDict['channel'])
                pubsub.unsubscribe(messageDict["channel"])       
                return 1
        return -1

    def controlProcess(message, pubsub):
        print('=============== controlProcess start ===============')
        print('check message["data"] in controlProcess :', message['data'])
        messageDict = json.loads(message['data'])
        print('check messageDict in controlProcess', messageDict)
        if messageDict.get('usage', None) is None:
            return 0
        elif messageDict.get("usage", None) == "pubsub":
            subscribeProcess(messageDict, pubsub)
        return -1
    def event_stream():
        try:
            pubsub = appRedis.pubsub()
            pubsub.id = clientId   
            pubsub.subscribe('admin_channel')
            while True:
                message = pubsub.get_message(timeout=10)
                if not message:
                    # print("ping")
                    yield "data: {}\n\n"
                    continue
                if type(message['data']) is not int:
                    if controlProcess(message, pubsub)==1:
                        yield "data: {}\n\n"
                        continue
                    else:
                        if controlProcess(message, pubsub)!=0:
                            continue
                        yield 'data: %s\n\n' % message["data"]
        except GeneratorExit:
            print('generatorExit...')
        finally:
            pubsub.reset()
    print('check clientNumber(get_pushes ..) : ', len(appRedis.client_list()))
    return Response(event_stream(), mimetype="text/event-stream")

# 해당 채널에 메시지를 보냄
@app.route('/post', methods=["POST"])
def publish_data():
    """
    requestBody = {
        "channel" : "target_channel ...",
        "data" : "your_data_content ..."
    }    
    """
    requestBody = request.get_json()
    appRedis.publish(requestBody['channel'], json.dumps(requestBody))    
    return 'publish_data ...'

@app.route('/chat', methods=["POST"])
def chat():
    """
    requestBody = {
        "channel":"target_channel ...",
        "speaker":"speaker ...",
        "messageContent":"message content ..."
    }
    """
    requestBody = request.get_json()
    appRedis.publish(requestBody['channel'], json.dumps(requestBody))
    return 'aa..'

@app.route('/pubsub', methods=["POST"])
def doPubsub():
    """
    requestBody = {
        "usage":"pubsub",
        "id" : "target_client_id",
        "channel" : "target_channel ...",
        "subscribe_flag" : "subscribe or unsubscribe"
    }
    """
    requestBody = request.get_json()
    requestBody["usage"] = 'pubsub'
    appRedis.publish("admin_channel", json.dumps(requestBody))    
    return 'pubsub process ...'

if __name__ == '__main__':
    app.run(host="192.168.0.51", port="5000", debug=True)
    # app.run(host="127.0.0.1", port="5000")
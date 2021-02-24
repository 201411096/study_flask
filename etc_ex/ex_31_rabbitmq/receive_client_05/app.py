# flask_socketio를 이용

# ========================================================================================================================
# Error_01
# WebSocket transport not available. Install eventlet or gevent and gevent-websocket for improved performance.
# Solution
# pip install eventlet
# ========================================================================================================================
# Error_02
# Flask socketio blocked by something during time.sleep
# Solution
# time.sleep() => socketio.sleep()
# Thread().start() => socketio.start_background_task()
# ========================================================================================================================
# Error_03
# socketio.start_background_task()에 인자를 전달하지 못하는 문제
# Solution
# lambda 사용
# ========================================================================================================================

from flask import Flask, Response, render_template, request, session, escape
from flask_cors import CORS
from flask_socketio import SocketIO
import queue
import pika, sys, os, json
from threading import Thread

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, ping_timeout=5)

myRabbitMQ_config = {
    "username":"abc",
    "password":"abc",
    "hostip":"192.168.0.51",
    "port":"5672"
}

@app.route('/')
def render_template_sample():
    return render_template('sample.html')

@app.route("/getQueueDataList")
def getQueueDataList():
    def getDataListFromMQ(queueName, auto_ack_flag):
        messageList = []
        credentials = pika.PlainCredentials(username=myRabbitMQ_config['username'], password=myRabbitMQ_config['password'])
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=myRabbitMQ_config['hostip'], port=myRabbitMQ_config['port'], credentials=credentials))
        channel = connection.channel()
        channel.queue_declare(queue=queueName)

        while True:
            evt_method, evt_properties, evt_body = channel.basic_get(queueName, auto_ack=auto_ack_flag)
            if evt_method is None:
                connection.close()
                break
            else:
                messageList.append(json.loads(evt_body))
        return messageList

    auto_ack_flag = request.args.get('auto_ack', False)
    if auto_ack_flag == 'True':
        auto_ack_flag = True
    queueName = 'queue_name_01'

    messageList = getDataListFromMQ(queueName, auto_ack_flag)

    result = {}
    print('messageList : ', messageList)
    result['data'] = messageList
    return result

@app.route('/sendData', methods=["POST"])
def sendData():
    def sendDataToMQ(data):
        credentials = pika.PlainCredentials(username=myRabbitMQ_config['username'], password=myRabbitMQ_config['password'])
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=myRabbitMQ_config['hostip'], port=myRabbitMQ_config['port'], credentials=credentials))
        channel = connection.channel()

        queue_name = data.get('queueName', None)    
        channel.queue_declare(queue=queue_name)    

        myMessage = data
        myMessage = json.dumps(myMessage)
        channel.basic_publish(exchange='', routing_key=queue_name, body=myMessage)
        connection.close()    

    requestData = request.get_json()
    sendDataToMQ(requestData)
    result = {"sendData":"complete"}
    return result

@socketio.on('connect')
def socket_connect():
    print('connect ...')


@socketio.on('disconnect')
def socket_disconnect():
    print('disconnect ...')

@socketio.on('message')
def handle_message(data):
    print('received message: ', data)

# eventstream 역할
@socketio.on('join_queue')
def join_queue(data):
    def getDataListFromMQ(queueName, auto_ack_flag):
        messageList = []
        credentials = pika.PlainCredentials(username=myRabbitMQ_config['username'], password=myRabbitMQ_config['password'])
        connection = pika.BlockingConnection(pika.ConnectionParameters(host=myRabbitMQ_config['hostip'], port=myRabbitMQ_config['port'], credentials=credentials))
        channel = connection.channel()
        channel.queue_declare(queue=queueName)
        while True:
            evt_method, evt_properties, evt_body = channel.basic_get(queueName, auto_ack=auto_ack_flag)
            if evt_method is None:
                connection.close()
                break
            else:
                messageList.append(json.loads(evt_body))
        return messageList

    def getDataListFromMQAndSendThroughSocket(socketio, queueName, auto_ack_flag):
        import time, traceback
        while True:
            try:
                # time.sleep(2) # time.sleep() => socketio.sleep()
                socketio.sleep(2)
                messageList = getDataListFromMQ(queueName, auto_ack_flag)
                if len(messageList) == 0:
                    pass
                else:
                    data = {}
                    data['data'] = messageList
                    socketio.emit('dataStream', data)
            except:
                traceback.print_exc()

    auto_ack_flag = data.get("auto_ack", None)
    queueName = data.get('queueName', None)
    if auto_ack_flag == 'True':
        auto_ack_flag = True

    from threading import Thread
    # th = Thread(target=getDataListFromMQAndSendThroughSocket, args=[socketio, queueName, auto_ack_flag])          # Thread.start() => socketio.start_background_task()
    # th.start()
    socketio.start_background_task( (lambda a, b, c : getDataListFromMQAndSendThroughSocket(a, b, c)) (socketio, queueName, auto_ack_flag)  )

if __name__ == '__main__':
    socketio.run(app, host='192.168.0.51', port=5000, debug=True)
    # socketio.run(app, debug=True)
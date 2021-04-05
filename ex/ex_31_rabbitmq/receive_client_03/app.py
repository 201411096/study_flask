# rabbitmq와 event-stream을 같이 사용

from flask import Flask, Response, render_template, request, session, escape
from flask_cors import CORS
import queue
import pika, sys, os, json
from threading import Thread

app = Flask(__name__)
CORS(app)

myRabbitMQ_config = {
    "username":"abc",
    "password":"abc",
    "hostip":"192.168.0.51"
}

@app.route('/')
def render_template_sample():
    return render_template('sample.html')

@app.route("/getQueueDataList")
def getQueueDataList():
    auto_ack_flag = request.args.get('auto_ack', False)
    if auto_ack_flag == 'True':
        auto_ack_flag = True
    
    def getDataListFromMQ(queueName, auto_ack_flag):
        messageList = []
        credentials = pika.PlainCredentials(username=myRabbitMQ_config['username'], password=myRabbitMQ_config['password'])
        connection = pika.BlockingConnection(pika.ConnectionParameters(myRabbitMQ_config['hostip'], credentials=credentials))
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
    queueName = 'queue_name_01'

    messageList = getDataListFromMQ(queueName, auto_ack_flag)

    result = {}
    print('messageList : ', messageList)
    result['data'] = messageList
    return result

@app.route('/sendData', methods=["POST"])
def sendData():
    requestData = request.get_json()

    credentials = pika.PlainCredentials(username=myRabbitMQ_config['username'], password=myRabbitMQ_config['password'])
    connection = pika.BlockingConnection(pika.ConnectionParameters(myRabbitMQ_config['hostip'], credentials=credentials))
    channel = connection.channel()

    queue_name = requestData.get('queueName', None)    
    channel.queue_declare(queue=queue_name)    

    myMessage = requestData
    myMessage = json.dumps(myMessage)
    channel.basic_publish(exchange='', routing_key=queue_name, body=myMessage)
    connection.close()
    result = {"sendData":"complete"}
    return result

@app.route('/eventStream')
def func_eventStream():    
    def getDataListFromMQ(queueName, auto_ack_flag):
        messageList = []
        credentials = pika.PlainCredentials(username=myRabbitMQ_config['username'], password=myRabbitMQ_config['password'])
        connection = pika.BlockingConnection(pika.ConnectionParameters(myRabbitMQ_config['hostip'], credentials=credentials))
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
    def wrapper_consume(auto_ack_flag, queueName):
        import time
        import traceback
        while True:
            try:
                messageList = getDataListFromMQ(queueName, auto_ack_flag)
                if len(messageList) == 0:
                    yield 'event: {}\ndata: {}\n\n'
                else:
                    for i in range(len(messageList)):
                        queueData = messageList[i]
                        yield 'event: {}\ndata: {}\n\n'.format(queueData.get('event', ''), queueData.get('message', ''))
                time.sleep(2)
            except:
                traceback.print_exc()
                print('disconnected ...')
    auto_ack_flag = request.args.get('auto_ack', False)
    queueName = request.args.get('queueName', None)
    if auto_ack_flag == 'True':
        auto_ack_flag = True                
    return Response(wrapper_consume(auto_ack_flag, queueName), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(host="localhost", port="5000", debug=True)
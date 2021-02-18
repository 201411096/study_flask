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

@app.route('/data')
def make_sample_data():
    result = {"data":"myData"}
    return result

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

@app.route("/getQueueData")
def getQueueData():    
    def getDataFromMQ(queueName):
        returnData = None
        credentials = pika.PlainCredentials(username=myRabbitMQ_config['username'], password=myRabbitMQ_config['password'])
        connection = pika.BlockingConnection(pika.ConnectionParameters(myRabbitMQ_config['hostip'], credentials=credentials))
        channel = connection.channel()
        
        channel.queue_declare(queue=queueName)
        evt_method, evt_properties, evt_body = channel.basic_get(queueName)
        if evt_method is None:
            connection.close()
            returnData = json.loads('{}')
        else:
            returnData = json.loads(evt_body)
            channel.basic_ack(evt_method.delivery_tag)
        return returnData

    queueName = 'queue_name_01'
    message = getDataFromMQ(queueName)

    result = {}
    print('message : ', message)
    result['data'] = message
    return result

# @app.route('/sendData', methods=["POST"])
@app.route('/sendData')
def sendData():
    # requestData = request.get_json()
    requestData = {"e":"ee", "f":"ff"}

    credentials = pika.PlainCredentials(username=myRabbitMQ_config['username'], password=myRabbitMQ_config['password'])
    connection = pika.BlockingConnection(pika.ConnectionParameters(myRabbitMQ_config['hostip'], credentials=credentials))
    channel = connection.channel()

    queue_name = 'queue_name_01'
    channel.queue_declare(queue=queue_name)    

    myMessage = requestData
    myMessage = json.dumps(myMessage)
    channel.basic_publish(exchange='', routing_key=queue_name, body=myMessage)
    connection.close()
    result = {"sendData":"complete"}
    return result

@app.route('/test/eventStream')
def test_eventStream():
    def wrapper_consume():
        # while True:
        for i in range(100):
            yield 'a'
    return Response(wrapper_consume(), mimetype='text/event-stream')

@app.route('/test/eventStream2')
def test_eventStream2():
    import time
    def wrapper_consume():
        while True:
            time.sleep(1)
            yield 'a'
    return Response(wrapper_consume(), mimetype='text/event-stream')


if __name__ == '__main__':
    app.run(host="localhost", port="5000", debug=True)
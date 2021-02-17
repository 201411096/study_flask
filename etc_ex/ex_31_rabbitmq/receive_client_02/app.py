from flask import Flask, Response, render_template, request, session, escape
from flask_cors import CORS
import queue
import pika, sys, os, json
from threading import Thread

app = Flask(__name__)
CORS(app)

@app.route('/')
def render_template_sample():
    return render_template('sample.html')

@app.route('/data')
def make_sample_data():
    result = {"data":"myData"}
    return result

@app.route("/getQueueData")
def getQueueData():
    # def callBack(ch, method, properties, body):
    #     print('body : ', body)
    
    def messageProcessing(connection, channel, messageList, queueName):
        while True:
            evt_method, evt_properties, evt_body = channel.basic_get(queueName)
            if evt_method is None:
                print('evt_method is None ...')
                connection.close()
                break
            else:
                print('evt_method is not None ...')
                messageList.append(json.loads(evt_body) )
        return messageList
    messageList = []

    credentials = pika.PlainCredentials(username='abc', password='abc')
    connection = pika.BlockingConnection(pika.ConnectionParameters('192.168.0.51', credentials=credentials))
    channel = connection.channel()

    queue_name = 'queue_name_01'
    channel.queue_declare(queue=queue_name)

    # channel.basic_consume(queue=queue_name, on_message_callback=callBack)
    
    # channel.start_consuming()
    # Thread(target=channel.start_consuming).start()
    th = Thread(target=messageProcessing, args=[connection, channel, messageList, queue_name])
    th.start()

    th.join()
    result = {}
    print('messageList : ', messageList)
    result['data'] = messageList
    return result

if __name__ == '__main__':
    app.run(host="localhost", port="5000", debug=True)
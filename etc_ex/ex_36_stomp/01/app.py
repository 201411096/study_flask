# ====================================================================================================
# 1. edit Configuration file
# ====================================================================================================
# 2. Enabling rabbitmq_stomp
# .\rabbitmq-plugins.bat enable rabbitmq_stomp
# ====================================================================================================
# 3. Enabling rabbitmq_web_stomp
# .\rabbitmq-plugins.bat enable rabbitmq_web_stomp
# ====================================================================================================
# 4. check enabled plugins
# .\rabbitmq-plugins.bat list -e
# ====================================================================================================
# 5. rabbitmq config sample
# https://github.com/rabbitmq/rabbitmq-server/blob/v3.7.x/deps/rabbit/docs/rabbitmq.config.example
# ====================================================================================================

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
    return render_template('test.html')

if __name__ == '__main__':
    app.run(host="192.168.0.51", port="5000", debug=True)
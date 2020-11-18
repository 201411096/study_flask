# references
# https://maxhalford.github.io/blog/flask-sse-no-deps/

from flask import Flask, Response, render_template, request, session, escape
from flask_cors import CORS
import queue

app = Flask(__name__)
CORS(app)

class MessageAnnouncer:
    
    def __init__(self):
        self.listeners = []

    def listen(self):
        q = queue.Queue(maxsize=5)
        self.listeners.append(q)
        return q

    def announce(self, msg):
        for i in reversed(range(len(self.listeners))):
            try:
                self.listeners[i].put_nowait(msg)
            except queue.Full:
                del self.listeners[0]

announcer = MessageAnnouncer()

@app.route('/')
def hello_world():
    return 'Hello, World!'

def format_sse(data: str, event=None):
    msg = f'data: {data}\n\n'
    if event is not None:
        msg = f'event: {event}\n{msg}'
    return msg

@app.route('/ping')
def ping():
    msg = format_sse(data='pong')
    announcer.announce(msg=msg)
    return msg, 200

@app.route('/stream', methods=['GET'])
def stream():
    def event_stream():
        messages = announcer.listen()  # returns a queue.Queue
        while True:
            msg = messages.get()  # blocks until a new message arrives
            yield msg

    return Response(event_stream(), mimetype='text/event-stream')

@app.route('/sample')
def render_template_sample():
    return render_template('client.html')

if __name__ == '__main__':
    app.run(host="192.168.0.51", port="5000")
    # app.run(host="127.0.0.1", port="5000")
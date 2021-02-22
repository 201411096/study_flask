from flask import Flask, render_template, Response
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

# pip install flask-socketio
socketio = SocketIO(app)

@app.route('/')
def hello_world():
    return render_template('index.html')

@socketio.on('message')
def handle_message(data):
    print('received message: ' + data)

@socketio.on('message2')
def handle_message2(data):
    print('received message2: ' + data)

@socketio.on('connect')
def handle_message2():
    print('connect ...')

@socketio.on('disconnect')
def test_disconnect():
    print('disconnected ...')

if __name__ == '__main__':
    socketio.run(app, debug=True)
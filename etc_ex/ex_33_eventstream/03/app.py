from flask import Flask, render_template, Response
app = Flask(__name__)
import queue

myQueue = queue.Queue(maxsize=10)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/eventstream')
def make_eventstream():
    def eventStream():
        import time
        import datetime
        import traceback
        while True:
            try:
                queueLength = myQueue.qsize()
                if queueLength == 0:
                    yield 'event: {}\ndata: {}\n\n'
                else:
                    for i in range(queueLength):
                        queueData = myQueue.get_nowait()
                        yield 'event: {}\ndata: {}\n\n'.format(queueData.get('event', ''), queueData.get('message', ''))
                time.sleep(2)
            except:
                # pass
                traceback.print_exc()
                print('disconnected ..')
    return Response(eventStream(), mimetype='text/event-stream')

@app.route('/sendData')
def sendData():
    queueData = {}
    queueData['event'] = 'message'
    queueData['message'] = 'data...'
    myQueue.put(queueData)
    result = {"sendData":"1"}
    return result

if __name__ == '__main__':
    app.run(debug=True)
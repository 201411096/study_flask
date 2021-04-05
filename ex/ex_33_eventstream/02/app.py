# 데이터를 한번에 가져오지 못함 (queue에 3~4개의 데이터가 들어갔을 때도 2초에 하나씩 가져옴)

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
                time.sleep(2)
                queueData = {}
                if myQueue.empty():
                    pass
                else:
                    queueData = myQueue.get_nowait()
                    print('myQueueLen : ', myQueue.qsize())
                try:
                    yield 'event: {}\ndata: {}\n\n'.format(queueData.get('event', ''), queueData.get('message', ''))
                except:
                    yield 'event: {}\ndata: {}\n\n'
            except:
                traceback.print_exc()

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
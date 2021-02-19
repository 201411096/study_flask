from flask import Flask, render_template, Response
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/eventstream')
def make_eventstream():
    def eventStream():
        import time
        import datetime
        import traceback
        try:
            while True:
                time.sleep(1)
                print('send data ... ' + str(datetime.datetime.today()))
                
                # yield format
                # 1. 'data: {}\n\n'.format(data_content)
                # 2. 'event: {}\ndata: {}\n\n'.format(event_name, data_content)
                # 띄워쓰기 위치, \n 개수가 바뀌어도 이상하게 작동함

                yield 'event: {}\ndata: {}\n\n'.format('message', 'data')
                yield 'event: {}\ndata: {}\n\n'.format('message2', 'data2')        
        except:
            traceback.print_exc()
            # print('generator exception ...')
        finally:
            print('connection close ...')

    return Response(eventStream(), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True)
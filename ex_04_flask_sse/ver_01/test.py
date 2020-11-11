# redis 설치
# redis MS Open Tech Github
# https://github.com/microsoftarchive/redis
# redis MS Open Tech Github Release
# https://github.com/MSOpenTech/redis/releases
# Redis-x64-3.0.504.msi
# redis 설치 직후 실행 순서
# redis-cli.exe
# shutdown
# exit
# redis-server.exe
# sample 예시 reference : https://pypi.org/project/Flask-SSE/
from flask import Flask, Response, render_template
from flask_sse import sse
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config["REDIS_URL"]="redis://localhost"
app.register_blueprint(sse, url_prefix='/stream')

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/sample01')
def render_template_sample():
    return render_template('client.html')

@app.route('/send')
def send_message():
    sse.publish({"message": "Hello!"}, type='greeting')
    return "Message sent!"

@app.route('/event_01')
def event_01():
    sse.publish({"message": "event_01!"}, type='event_01')
    return "Message sent.. event_01.."

@app.route('/event_02')
def event_02():
    sse.publish({"message": "event_02!"}, type='event_02')
    return "Message sent.. event_02.."

if __name__ == '__main__':
     app.run(host="127.0.0.1", port="5000")
# redis 설치
# redis MS Open Tech Github
# https://github.com/microsoftarchive/redis
# redis MS Open Tech Github Release
# https://github.com/MSOpenTech/redis/releases
# redis 설치 직후 실행 순서
# redis-cli.exe
# shutdown
# exit
# redis-server.exe
from flask import Flask, Response
from flask_sse import sse

app = Flask(__name__)
app.config["REDIS_URL"]="redis://localhost"
app.register_blueprint(sse, url_prefix='/stream')

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/send')
def send_message():
    sse.publish({"message": "Hello!"}, type='greeting')
    return "Message sent!"

if __name__ == '__main__':
     app.run(host="127.0.0.1", port="8080")
from flask import Flask
from flask import g # 글로벌 객체(application context ... ) <-> request context

app = Flask(__name__) # 바로 실행될경우 __name__은 main...
app.debug = True # use only debug

@app.before_request
def before_request():
    print("before_request...")
    g.str = "한글"

@app.route("/gg")
def hello_world2():
    # getattr() -> (-, -, default_value)
    return 'musicplaylist...' + getattr(g, 'str', '111') # return -> response_value
    
@app.route("/")
def hello_world():
    return 'musicplaylist...'
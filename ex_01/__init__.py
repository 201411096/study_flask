from flask import Flask, Response, make_response, g, request, session
from datetime import datetime, date, timedelta
# from flask import g # 글로벌 객체(application context ... ) <-> request context

app = Flask(__name__) # 바로 실행될경우 __name__은 main...
app.debug = True # use only debug # app.config['debug']=True ..

# app.config['SERVER_NAME'] = 'local.com:5000' # hosts파일 수정해서 해봤는데 안됨

app.config.update(
    SECRET_KEY="X12343yRH!mMwf", # 암호화에 사용하는 값
    SESSION_COOKIE_NAME='pyweb_flask_session',
    PERMANENT_SESSION_LIFETIME=timedelta(31) # 31일동안 유지 ... 
)

@app.route('/wc') # write cookie ...
def wc():
    key = request.args.get('key')
    val = request.args.get('val')
    res = Response("SET COOKIE")
    res.set_cookie(key, val)
    session['Token'] = '123X' # session  ...
    return make_response(res)

@app.route('/rc') # read cookie ...
def rc():
    key = request.args.get('key')
    val = request.cookies.get(key)
    return "cookie['"+key+"'] = " + val + ", " + session.get('Token')

@app.route('/delsess')
def delsess():
    if session.get('Token'):
        del session['Token']
    return "Session이 삭제되었습니다!"

@app.route('/reqenv') # request environment ...
def reqenv():
    print(">> is_xhr=", request.is_xhr)
    print(">> json =", request.get_json())
    return ('REQUEST_METHOD: %(REQUEST_METHOD) s <br>'
    'SCRIPT_NAME: %(SCRIPT_NAME) s <br>'
    'PATH_INFO: %(PATH_INFO) s <br>'
    'QUERY_STRING: %(QUERY_STRING) s <br>'
    'SERVER_NAME: %(SERVER_NAME) s <br>'
    'SERVER_PORT: %(SERVER_PORT) s <br>'
    'SERVER_PROTOCOL: %(SERVER_PROTOCOL) s <br>'
    'wsgi.version: %(wsgi.version) s <br>'
    'wsgi.url_scheme: %(wsgi.url_scheme) s <br>'
    'wsgi.input: %(wsgi.input) s <br>'
    'wsgi.errors: %(wsgi.errors) s <br>'
    'wsgi.multithread: %(wsgi.multithread) s <br>'
    'wsgi.multiprocess: %(wsgi.multiprocess) s <br>'
    'wsgi.run_once: %(wsgi.run_once) s') % request.environ

def ymd(fmt):
    # nested function은 성능상의 이점도 존재...?..
    def trans(date_str):
        return datetime.strptime(date_str, fmt)
    return trans

@app.route("/dt")
def dt():
    datestr = request.values.get('date', date.today(), type=ymd('%Y-%m-%d')) # 두번째 인자(default값 -> 값이 넘어오지 않았을 경우) # 세번째 인자 => 타입 처리(함수를 인자로 넘김)
    return "우리나라 시간 형식: " + str(datestr)

@app.route("/sd")
def helloworld_local():
    return "Hello Local.com!"

@app.route("/sd", subdomain="g")
def helloworld():    
    return "Hello G.Local.com!!!"

@app.route('/rp')
def rp():
    # q = request.args.get('q')
    q = request.args.getlist('q')
    return "q= %s" % str(q)

#WSGI(WebServer Gateway Interface)
@app.route('/test_wsgi')
def wsgi_test():
    def application(environ, start_response):
        body = 'The request method was %s' % environ['REQUEST_METHOD']
        headers = [('Content-Type', 'text/plain'), ('Content-Length', str(len(body)))]
        start_response('200 OK', headers)
        return [body]
    return make_response(application)
@app.route("/res1")
def res1():
    custom_res = Response("custom response...", 200, {'test':'ttt'})
    return make_response(custom_res)

# @app.before_request
# def before_request():
#     print("before_request...")
#     g.str = "한글"

@app.route("/gg")
def hello_world2():
    # getattr() -> (-, -, default_value)
    return 'ex01...' + getattr(g, 'str', '111') # return -> response_value

@app.route("/")
def hello_world():
    return 'ex01...'
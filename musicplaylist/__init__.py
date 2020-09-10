from flask import Flask, Response, make_response, g, request
# from flask import g # 글로벌 객체(application context ... ) <-> request context

app = Flask(__name__) # 바로 실행될경우 __name__은 main...
app.debug = True # use only debug # app.config['debug']=True ..

# app.config['SERVER_NAME'] = 'local.com:5000' # hosts파일 수정해서 해봤는데 안됨
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
    return 'musicplaylist...' + getattr(g, 'str', '111') # return -> response_value

@app.route("/")
def hello_world():
    return 'musicplaylist...'
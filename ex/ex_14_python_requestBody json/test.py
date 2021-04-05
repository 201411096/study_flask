from flask import Flask, Response, make_response, g, request, session
import json
app = Flask(__name__) # 바로 실행될경우 __name__은 main...
app.debug = True # use only debug # app.config['debug']=True ..

@app.route('/test')
def test():
    print(request)
    requestJson = request.get_json() # requestBody 를 json의 형태로 변환해서 가져옴(python dict)
    
    print('dict ..', requestJson)
    print('type ..' , type(requestJson))
    
    res = Response(json.dumps(requestJson))
    return make_response(res)

app.run(host="127.0.0.1", port="7080")
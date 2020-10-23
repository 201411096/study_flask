from flask import Flask, Response, make_response, g, request, session
import json
app = Flask(__name__) # 바로 실행될경우 __name__은 main...
app.debug = True # use only debug # app.config['debug']=True ..

@app.route('/test')
def test():
    print('request ..', request)
    print(request.args.get('id1'))
    print(request.args.get('id2'))
    requestJson = request.get_json() # requestBody 를 json의 형태로 변환해서 가져옴(python dict)
    dictData = requestJson
    
    print('dict ..', dictData)
    print('type ..' , type(dictData))

    print()
    
    print(request.args.get('id1'))
    print(request.args.get('id2'))
    res = Response('abc')
    return make_response(res)

# pathVariable <-> queryString
# pathVariable
# ex) ../test2/33
# queryString
# ex) ../test2?id3=33
@app.route('/test2/<id3>') # id3는 queryString과 상관없은 pathVariable
def test2(id3):
    print('request ..', request)
    requestJson = request.get_json() # requestBody 를 json의 형태로 변환해서 가져옴(python dict)
    dictData = requestJson
    
    print('dict ..', dictData)
    print('type ..' , type(dictData))
    
    print(request.args.get('id1'))
    print(request.args.get('id2'))
    print(request.args.get('id3'))
    print('id3 ..', id3)
    res = Response('abc')
    return make_response(res)

#request.args.get <-> request.get_json() 차이 확인 (request.args.get은 queryString의 내용만을 가져옴)
def test3():
    print('request ..', request)
    print(request.args.get('id1')) 
    print(request.args.get('id2'))
    requestJson = request.get_json() # requestBody 를 json의 형태로 변환해서 가져옴(python dict)
    dictData = requestJson
    
    print('dict ..', dictData)
    print('type ..' , type(dictData))

    print()
    
    print(request.args.get('id1'))
    print(request.args.get('id2'))
    res = Response('abc')
    return make_response(res)

app.run(host="127.0.0.1", port="7080")
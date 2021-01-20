from services import app
from flask import request, session, render_template, redirect
from flask import session as flaskSession
from services.member import service as member_service
# from services.board import service as board_service
from services.board import service_ver2 as board_service
from util import authDecorator

@app.route('/boardList', methods=['GET'])
def board_getList():
    resultData = {}
    resultData['boardList'] = board_service.board_getList()
    print('data(board_getList) : ', resultData)
    return resultData

@app.route('/board/write', methods=['POST'])
@authDecorator
def board_write():
    data = request.get_json()
    data['member_id'] = flaskSession.get('userData')['member_id']
    #210120 수정
    # 
    print('data(board_write) : ', data)

    resultData = board_service.board_write(data)

    return resultData

@app.route('/board/contentList', methods=["POST"])
@authDecorator
def board_contentList():
    data = {}
    result = {}
    requestData = request.get_json()
    print('data(board_contentList) : ', data)
    if requestData is not None:
        data.update(requestData)
    if data.get('page', None) is None:
        data['page'] = 1
    if data.get('numberInPage', None) is None:
        data['numberInPage'] = 10
    if data.get('searchWord', None) is None:
        data['searchWord'] = ''
    data['startrow'] = (int(data['page'])-1)*10

    result['boardListData'] = board_service.board_contentList(data)

    return result
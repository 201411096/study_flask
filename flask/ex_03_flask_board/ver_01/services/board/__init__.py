from services import app
from flask import request, session, render_template, redirect
from flask import session as flaskSession
from services.member import service as member_service
from services.board import service as board_service
from util import authDecorator
from services.authority import service as authority_service
from services.alarm import service as alarm_service

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

    # =============== 0205 알람기능 테스트 ===============
    alarmData = {}
    alarmData['board_content_id'] = board_service.get_last_boardContentId()
    alarmData['board_id'] = data['board_id']
    alarm_memberList = alarm_service.alarm_board_getMemberList(alarmData)
    alarmData['from_member_id'] = data['member_id']
    alarmData['alarm_content'] = data['board_content_title']
    print('================ alarm_board_getMemberList ===============')
    for alarm_member in alarm_memberList:
        # 자기 자신은 제외
        if alarm_member['member_id'] == data['member_id']:
            continue
        print(alarm_member)
        alarmData['to_member_id'] = alarm_member['member_id']
        alarm_service.alarm_board_send(alarmData)
    print('================ alarm_board_getMemberList ===============')
    # =============== 0205 알람기능 테스트 ===============
    return resultData

@app.route('/board/update', methods=['POST'])
@authDecorator
def board_update():
    data = request.get_json()
    resultData = board_service.board_update(data)

    return resultData

@app.route('/board/delete', methods=['POST'])
@authDecorator
def board_delete():
    data = request.get_json()
    resultData = board_service.board_delete(data)
    return resultData

@app.route('/board/list', methods=["POST"])
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
    print(result)
    return result
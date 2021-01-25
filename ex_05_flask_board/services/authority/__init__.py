from services import app
from flask import request, session, render_template, redirect
from flask import session as flaskSession
from services.member import service as member_service
from services.board import service_ver2 as board_service
from services.comment import service as comment_service
from services.authority import service as authority_service
from util import authDecorator

@app.route("/test/groupAuthority/getList", methods=['GET'])
@authDecorator
def authority_groupAuthority_getList():
    data = {}
    result = {}
    data['member_id'] = flaskSession.get('userData')['member_id']

    result['data'] = authority_service.authority_groupAuthority_getList(data)
    return result

@app.route("/test/boardAuthority/getList", methods=["GET"])
@authDecorator
def authority_boardAuthority_getList():
    data = {}
    result = {}
    data['member_id'] = flaskSession.get('userData')['member_id']

    result['data'] = authority_service.authority_boardAuthority_getList(data)
    return result

@app.route('/authority/getList', methods=["GET"])
@authDecorator
def authority_getList():
    result = authority_service.getAuthorityList()
    return result

@app.before_request
def before_request():
    deniedFlag = 0
    requestPath = request.path
    print('myRequestPath : ', requestPath)

    # 게시판, 댓글관련 api 처리
    if requestPath.startswith('/board/') or requestPath.startswith('/comment/'):
        requestData = request.get_json()
        requestTarget = requestPath.split('/')[1]
        requestRole = requestPath.split('/')[2]
        if requestRole == 'list':
            requestRole = 'read'
        print('myRequestRole : ', requestRole)
        print('myRequestTarget : ', requestTarget)
        if requestData is not None:
            print("myRequestData : ",  requestData)
            boardIdInRequestData = requestData.get('board_id', None)
            if boardIdInRequestData is None:
                deniedFlag = 1
            else:
                currentUserAuthority = authority_service.getAuthorityList()
                authorityForCurrentRequest = currentUserAuthority['authority_board'][boardIdInRequestData]['authority_board_content_'+requestRole]
                if authorityForCurrentRequest == '0':
                    deniedFlag = 1
                elif (authorityForCurrentRequest == '1') and (requestRole=='update' or requestRole =='delete'):
                    if requestTarget == 'board':
                        dataForQuery = {}
                        dataForQuery['board_content_id'] = requestData['board_content_id']
                        contentMemberId = board_service.board_content(dataForQuery)[0]['member_id']
                        currentMemberId = flaskSession.get('userData')['member_id']
                        if currentMemberId != contentMemberId:
                            deniedFlag=1
                        contentBoardId = board_service.board_content(dataForQuery)[0]['board_id']
                        if contentBoardId != boardIdInRequestData:
                            deniedFlag=1
                    elif requestTarget =='comment':
                        dataForQuery = {}
                        dataForQuery['comment_id'] = requestData['comment_id']
                        contentMemberId = comment_service.commet_content(dataForQuery)[0]['member_id']
                        currentMemberId = flaskSession.get('userData')['member_id']
                        if currentMemberId != contentMemberId:
                            deniedFlag=1
                        contentBoardId = board_service.board_content(dataForQuery)[0]['board_id']
                        if contentBoardId != boardIdInRequestData:
                            deniedFlag=1
    elif requestPath.startswith('/render/board'):
        # 사용하지 않는 부분
        requestRole = requestPath.split('/render/board')[1]
        requestRole = requestRole.split('/')[0].lower()
        if requestRole == 'content':
            requestRole = 'read'
        print('myRequestRole : ', requestRole)
                    
    if deniedFlag == 1:
        print('deniedFlag : ', deniedFlag)
        result = {}
        result['code']='22'
        result['description']='insufficient authority'
        return result

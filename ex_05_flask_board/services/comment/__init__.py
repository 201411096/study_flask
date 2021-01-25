from services import app
from flask import request, session, render_template, redirect
from flask import session as flaskSession
from services.member import service as member_service
from services.board import service as board_service
from services.comment import service as comment_service
from util import authDecorator
from services.authority import service as authority_service

@app.route('/comment/write', methods=['POST'])
@authDecorator
def comment_write():
    data = request.get_json()
    data['member_id'] = flaskSession.get('userData')['member_id']
    result = {}
    result = comment_service.comment_write(data)
    return result

@app.route('/comment/list', methods=['POST'])
@authDecorator
def comment_list():
    data = request.get_json()
    data['member_id'] = flaskSession.get('userData')['member_id']
    result={}
    result['commentListData'] = comment_service.comment_contentList(data)
    return result

@app.route('/comment/delete', methods=['POST'])
@authDecorator
def comment_delete():
    data = request.get_json()
    result = comment_service.comment_delete(data)
    return result
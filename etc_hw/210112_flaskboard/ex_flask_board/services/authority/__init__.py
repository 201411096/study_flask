from services import app
from flask import request, session, render_template, redirect
from flask import session as flaskSession
from services.member import service as member_service
from services.board import service_ver2 as board_service
from services.authority import service as authority_service
from util import authDecorator

@app.route("/test/groupAuthority/getList", methods=['GET'])
def authority_groupAuthority_getList():
    data = {}
    result = {}
    data['member_id'] = flaskSession.get('userData')['member_id']

    result['data'] = authority_service.authority_groupAuthority_getList(data)
    return result

@app.route("/test/boardAuthority/getList", methods=["GET"])
def authority_boardAuthority_getList():
    data = {}
    result = {}
    data['member_id'] = flaskSession.get('userData')['member_id']

    result['data'] = authority_service.authority_boardAuthority_getList(data)
    return result

@app.route('/test/authority/getList', methods=["GET"])
def authority_getList():
    result = authority_service.getAuthorityList()
    return result
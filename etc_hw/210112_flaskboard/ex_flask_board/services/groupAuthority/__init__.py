from services import app
from flask import request, session, render_template, redirect
from flask import session as flaskSession
from services.member import service as member_service
from services.board import service_ver2 as board_service
from services.groupAuthority import service as groupAuthority_service
from util import authDecorator

@app.route('/groupAuthority/getList', methods=['POST'])
def groupAuthority_getList():
    data = request.get_json()
    result = {}
    result['data'] = groupAuthority_service.groupAuthority_getList(data)
    print(result)
    return result
from services import app
from flask import request, session, render_template, redirect
from services.member import service as member_service
from services.board import service as board_service

@app.route('/boardList', methods=['GET'])
def board_getList():
    resultData = {}
    resultData['boardList'] = board_service.board_getList()
    print('data(board_getList) : ', resultData)
    return resultData

@app.route('/board/write', methods=['POST'])
def board_write():
    data = request.get_json()
    print('data(board_write) : ', data)
    return redirect('/render/index')
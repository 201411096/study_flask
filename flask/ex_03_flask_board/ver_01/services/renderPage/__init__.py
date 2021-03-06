from services import app
from flask import render_template, request, redirect
from flask import session as flaskSession
from util import authDecorator
from services.board import service as board_service
from services.authority import service as authority_service
from services.alarm import service as alarm_service

@app.route('/test/renderPage')
def test_renderPage():
	return render_template('test_sample.html')

@app.route('/test/test_loginSuccess')
@authDecorator
def test_loginSuccess():
	print('check userData : ', flaskSession.get('userData'))
	return render_template('test_loginSuccess.html')

@app.route('/test/api')
@authDecorator
def test_api():
	return render_template('test_api.html')

@app.route('/test/boardlistView')
@authDecorator
def render_boardlistView():	
	return render_template('test_boardlistView.html')

@app.route('/render/login')
def render_login():
	return render_template('login.html')

@app.route('/render/signup')
def render_signup():
	return render_template('signup.html')

@app.route('/render/index')
def render_index():
	return render_template('index.html')

@app.route('/render/boardWrite')
@authDecorator
def render_boardWrite():
	data = {}
	data['test1']='test11'
	data['test2']='test2'
	
	requestParameter = request.args.to_dict()
	print('request.args(render_boardWrite) : ', requestParameter)

	if requestParameter is not None:
		data.update(requestParameter)
	
	return render_template('boardWrite.html', data=data)

@app.route('/render/boardUpdate')
@authDecorator
def render_boardUpdate():
	requestParameter = request.args.to_dict()
	print('request.args(render_boardUpdate) : ', requestParameter)

	data = board_service.board_content(requestParameter)[0]


	return render_template('boardUpdate.html', data=data)

@app.route('/render/boardContent/<board_content_id>')
@authDecorator
def render_boardContent(board_content_id):
	requestData={}
	data = {}
	requestData['board_content_id']=board_content_id
	data = board_service.board_content(requestData)[0]
	data['authority'] = authority_service.getAuthorityList()

	# print('board_content_deleted : ', data['board_content_deleted'])
	if(data['board_content_deleted']=='Y'):
		# print('if문 작동확인')
		return redirect('/render/notice_board_content_deleted')

	# print('resultData(render_boardContent) : ', data)

	# =============== 0208 알람기능 테스트 ===============
	alarmData = {}
	alarmData['board_content_id'] = data['board_content_id']
	alarmData['to_member_id'] = flaskSession.get('userData')['member_id']
	alarm_service.alarm_read(alarmData)
	# =============== 0208 알람기능 테스트 ===============

	return render_template('boardContent.html', data=data)

@app.route('/render/notice_board_content_deleted')
def render_notice_board_content_deleted():
	return render_template('notice_board_content_deleted.html')

@app.route('/render/notice_required_authority')
def render_notice_required_authority():
	return render_template('notice_required_authority.html')
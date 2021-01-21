from services import app
from flask import request, session, render_template, redirect
from services.member import service as member_service


@app.route('/test/member')
def test_member():
	member_service.test_member_service()
	return "test_member..."

@app.route('/test/session')
def test_session():
	print('test_session : ', session.get('userData'))
	return '11'

@app.route('/test/getList')
def test_getList():
	resultData = member_service.test_getList()
	print(resultData)
	return '11'

@app.route('/member/signup', methods=['POST'])
def member_signup():
	data = request.get_json()
	return member_service.member_signup(data)

@app.route('/member/login', methods=['POST'])
def member_login():
	result = {}
	result['code'] = '-1'
	data = request.get_json()
	serviceResult = member_service.member_login(data)

	if(len(serviceResult)==0):
		result['code'] = '-1' # 해당 아이디가 존재하지 않음
	elif(serviceResult[0]['member_pw'] == data['member_pw']):
		result['code'] = '1' # 로그인 성공
		del serviceResult[0]['member_pw']
		session['userData'] = serviceResult[0]
	else:
		result['code'] = '0' # 패스워드가 일치하지 않음

	return result

@app.route('/member/logout')
def member_logout():
	session.clear()
	return redirect('/render/index')

@app.route('/member/getCurrentMemberData')
def member_getCurrentMemberData():
	result = {}
	data = {}
	
	data['member_id'] = session['userData']['member_id']
	serviceResult = member_service.member_login(data)
	result['data'] = serviceResult
	
	return result

# @app.route('/member/logincheck')
# def member_loginchk():
# 	resultData = {}
# 	userData = session.get('userData')
# 	if userData is None:
# 		print('userData is None ...')
# 		resultData['code'] = '0'
# 	else:
# 		print("session's userData : ", userData)
# 		resultData['code'] = '1'
# 	resultData['userData'] = userData
	
# 	return render_template('login.html')

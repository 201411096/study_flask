from services import app
from services.member import service as member_service
from flask import request

@app.route('/test/member')
def test_member():
	member_service.test_member_service()
	return "test_member..."

@app.route('/member/signup', methods=['POST'])
def member_signup():
	data = request.get_json()
	print("data(member_signup) : ", data)
	return member_service.member_signup(data)

@app.route('/member/login', methods=['POST'])
def member_login():
	data = request.get_json()
	print('data(member_login) : ', data)
	return member_service.member_login(data)
from __main__ import session
from dto import *
from sqlalchemy import exc
def test_member_service():
	member = Member(
		'aab', group_code='bb', member_pw='cc', member_name='dd', member_birthday='20120213', member_phonenumber='11', member_nickname='hh')
	session.add(member)
	session.commit()
	return 1
	

def member_signup(data):
	result = {}
	member = Member(
		data['member_id'], group_code='01', member_pw=data['member_pw'],
		member_name=data['member_name'], member_birthday=data['member_birthday'], member_phonenumber=data['member_phonenumber'],
		member_nickname=data['member_nickname']
	)
	try:
		session.add(member)
		session.commit()
		result['code'] = '1'
	except exc.IntegrityError:
		result['code'] = '0'
	return result
	
def member_login(data):
	return -1
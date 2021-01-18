from __main__ import session
from dto import *
from sqlalchemy import exc
from util import *
# PyJWT 1.7.1

def test_member_service():
	member = Member(
		'aab', group_code='bb', member_pw='cc', member_name='dd', member_birthday='20120213', member_phonenumber='11', member_nickname='hh')
	session.add(member)
	session.commit()
	return 1

def test_getList():
	resultData = session.query(Member).with_entities(Member.member_id, Member.member_name)
	return queryToDict(resultData)

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
		session.rollback()
		result['code'] = '0'
	return result
	
def member_login(data):
	queryData = session.query(Member).\
	with_entities(
	Member.member_id, Member.group_code, Member.member_name, Member.member_pw,
	Member.member_birthday, Member.member_phonenumber, Member.member_nickname).\
	filter(Member.member_id == data['member_id'])
	return queryToDict(queryData)
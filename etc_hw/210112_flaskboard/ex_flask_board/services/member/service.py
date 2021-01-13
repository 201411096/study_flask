from __main__ import session
from dto import *

def test_member_service():
  member = Member('aab', group_code='bb', member_pw='cc', member_name='dd', member_birthday='20120213', member_phonenumber='11', member_nickname='hh')
  session.add(member)
  session.commit()
  return
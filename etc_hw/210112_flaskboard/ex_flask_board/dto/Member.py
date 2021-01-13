from sqlalchemy import Column, Integer, VARCHAR, NUMERIC, CHAR, DATETIME, TEXT
from __main__ import Base

class Member(Base):
    __tablename__ = 'member' #회원 
    __table_args__ = {
            'comment' : '회원'
        }

    member_id                            = Column(VARCHAR(100), primary_key=True, comment='') # 
    group_code                           = Column(VARCHAR(100), comment='') # 
    member_pw                            = Column(VARCHAR(100), comment='') # 
    member_name                          = Column(VARCHAR(100), comment='') # 
    member_birthday                      = Column(DATETIME, comment='') # 
    member_phonenumber                      = Column(VARCHAR(100), comment='') # 
    member_nickname                      = Column(VARCHAR(100), comment='') # 

    def __init__(self, memberId, **kwargs):
        self.member_id = memberId

        self.group_code                    = kwargs.get('group_code', None)
        self.member_pw                     = kwargs.get('member_pw', None)
        self.member_name                   = kwargs.get('member_name', None)
        self.member_birthday               = kwargs.get('member_birthday', None)
        self.member_phonenumber            = kwargs.get('member_phonenumber', None)
        self.member_nickname               = kwargs.get('member_nickname', None)

    def __repr__(self):
        return "{'member_id' : '%s', \
        'group_code' : '%s', \
        'member_pw' : '%s', \
        'member_name' : '%s', \
        'member_birthday' : '%s', \
        'member_phonenumber' : '%s', \
        'member_nickname' : '%s'}" % (
                    self.member_id,
                    self.group_code,
                    self.member_pw,
                    self.member_name,
                    self.member_birthday,
                    self.member_phonenumber,
                    self.member_nickname)
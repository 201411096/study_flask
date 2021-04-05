from sqlalchemy import Column, Integer, VARCHAR, NUMERIC, CHAR, DATETIME, TEXT
from __main__ import Base

class MemberGroup(Base):
    __tablename__ = 'member_group' #회원그룹 
    __table_args__ = {
            'comment' : '회원그룹'
        }

    group_code                           = Column(VARCHAR(100), primary_key=True, comment='') # 
    group_name                           = Column(VARCHAR(100), comment='') # 
    group_des                            = Column(VARCHAR(1000), comment='') # 

    def __init__(self, groupCode, **kwargs):
        self.group_code = groupCode

        self.group_name                    = kwargs.get('group_name', None)
        self.group_des                     = kwargs.get('group_des', None)

    def __repr__(self):
        return "{'group_code' : '%s', \
        'group_name' : '%s', \
        'group_des' : '%s'}" % (
                    self.group_code,
                    self.group_name,
                    self.group_des)
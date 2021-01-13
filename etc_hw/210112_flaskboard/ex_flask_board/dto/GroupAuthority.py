from sqlalchemy import Column, Integer, VARCHAR, NUMERIC, CHAR, DATETIME, TEXT
from __main__ import Base

class GroupAuthority(Base):
    __tablename__ = 'group_authority' #그룹공통권한 
    __table_args__ = {
            'comment' : '그룹공통권한'
        }

    group_code                           = Column(VARCHAR(100), primary_key=True, comment='') # 
    authority_board_create                      = Column(VARCHAR(10), comment='') # 
    authority_board_update                      = Column(VARCHAR(10), comment='') # 
    authority_board_delete                      = Column(VARCHAR(10), comment='') # 

    def __init__(self, groupCode, **kwargs):
        self.group_code = groupCode

        self.authority_board_create        = kwargs.get('authority_board_create', None)
        self.authority_board_update        = kwargs.get('authority_board_update', None)
        self.authority_board_delete        = kwargs.get('authority_board_delete', None)

    def __repr__(self):
        return "{'group_code' : '%s', \
        'authority_board_create' : '%s', \
        'authority_board_update' : '%s', \
        'authority_board_delete' : '%s'}" % (
                    self.group_code,
                    self.authority_board_create,
                    self.authority_board_update,
                    self.authority_board_delete)
from sqlalchemy import Column, Integer, VARCHAR, NUMERIC, CHAR, DATETIME, TEXT
from __main__ import Base

class GroupBoardAuthority(Base):
    __tablename__ = 'group_board_authority' #그룹별게시판권한 
    __table_args__ = {
            'comment' : '그룹별게시판권한'
        }

    group_code                           = Column(VARCHAR(100), primary_key=True, comment='') # 
    board_id                             = Column(VARCHAR(100), primary_key=True, comment='') # 
    authority_board_content_read                      = Column(VARCHAR(10), comment='') # 
    authority_board_content_write                      = Column(VARCHAR(10), comment='') # 
    authority_board_content_update                      = Column(VARCHAR(10), comment='') # 
    authority_board_content_delete                      = Column(VARCHAR(10), comment='') # 

    def __init__(self, groupCode, **kwargs):
        self.group_code = groupCode

        self.board_id                      = kwargs.get('board_id', None)
        self.authority_board_content_read  = kwargs.get('authority_board_content_read', None)
        self.authority_board_content_write = kwargs.get('authority_board_content_write', None)
        self.authority_board_content_update= kwargs.get('authority_board_content_update', None)
        self.authority_board_content_delete= kwargs.get('authority_board_content_delete', None)

    def __repr__(self):
        return "{'group_code' : '%s', \
        'board_id' : '%s', \
        'authority_board_content_read' : '%s', \
        'authority_board_content_write' : '%s', \
        'authority_board_content_update' : '%s', \
        'authority_board_content_delete' : '%s'}" % (
                    self.group_code,
                    self.board_id,
                    self.authority_board_content_read,
                    self.authority_board_content_write,
                    self.authority_board_content_update,
                    self.authority_board_content_delete)
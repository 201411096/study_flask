from sqlalchemy import Column, Integer, VARCHAR, NUMERIC, CHAR, DATETIME, TEXT
from __main__ import Base

class BoardList(Base):
    __tablename__ = 'board_list' #게시판리스트 
    __table_args__ = {
            'comment' : '게시판리스트'
        }

    board_id                             = Column(VARCHAR(100), primary_key=True, comment='') # 
    board_name                           = Column(VARCHAR(100), comment='') # 
    board_des                            = Column(VARCHAR(1000), comment='') # 

    def __init__(self, boardId, **kwargs):
        self.board_id = boardId

        self.board_name                    = kwargs.get('board_name', None)
        self.board_des                     = kwargs.get('board_des', None)

    def __repr__(self):
        return "{'board_id' : '%s', \
        'board_name' : '%s', \
        'board_des' : '%s'}" % (
                    self.board_id,
                    self.board_name,
                    self.board_des)
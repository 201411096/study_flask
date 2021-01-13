from sqlalchemy import Column, Integer, VARCHAR, NUMERIC, CHAR, DATETIME, TEXT
from __main__ import Base

class Board(Base):
    __tablename__ = 'board' #게시판 
    __table_args__ = {
            'comment' : '게시판'
        }

    board_content_id                      = Column(VARCHAR(100), primary_key=True, comment='') # 
    board_content_pid                      = Column(VARCHAR(100), comment='') # 
    member_id                            = Column(VARCHAR(100), comment='') # 
    board_id                             = Column(VARCHAR(100), comment='') # 
    board_content_title                      = Column(VARCHAR(100), comment='') # 
    board_content_body                      = Column(VARCHAR(1000), comment='') # 
    board_content_regdatetime                      = Column(DATETIME, comment='') # 
    board_content_edtdatetime                      = Column(DATETIME, comment='') # 
    board_content_num                      = Column(VARCHAR(100), comment='') # 
    board_content_deleted                      = Column(VARCHAR(10), comment='') # 

    def __init__(self, boardContentId, **kwargs):
        self.board_content_id = boardContentId

        self.board_content_pid             = kwargs.get('board_content_pid', None)
        self.member_id                     = kwargs.get('member_id', None)
        self.board_id                      = kwargs.get('board_id', None)
        self.board_content_title           = kwargs.get('board_content_title', None)
        self.board_content_body            = kwargs.get('board_content_body', None)
        self.board_content_regdatetime     = kwargs.get('board_content_regdatetime', None)
        self.board_content_edtdatetime     = kwargs.get('board_content_edtdatetime', None)
        self.board_content_num             = kwargs.get('board_content_num', None)
        self.board_content_deleted         = kwargs.get('board_content_deleted', None)

    def __repr__(self):
        return "{'board_content_id' : '%s', \
        'board_content_pid' : '%s', \
        'member_id' : '%s', \
        'board_id' : '%s', \
        'board_content_title' : '%s', \
        'board_content_body' : '%s', \
        'board_content_regdatetime' : '%s', \
        'board_content_edtdatetime' : '%s', \
        'board_content_num' : '%s', \
        'board_content_deleted' : '%s'}" % (
                    self.board_content_id,
                    self.board_content_pid,
                    self.member_id,
                    self.board_id,
                    self.board_content_title,
                    self.board_content_body,
                    self.board_content_regdatetime,
                    self.board_content_edtdatetime,
                    self.board_content_num,
                    self.board_content_deleted)
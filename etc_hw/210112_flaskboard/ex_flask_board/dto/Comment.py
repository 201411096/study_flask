from sqlalchemy import Column, Integer, VARCHAR, NUMERIC, CHAR, DATETIME, TEXT
from __main__ import Base

class Comment(Base):
    __tablename__ = 'comment' #댓글 
    __table_args__ = {
            'comment' : '댓글'
        }
    # autoincrement
    # comment_id                           = Column(VARCHAR(100), primary_key=True, comment='') # 
    comment_id                           = Column(Integer, primary_key=True, autoincrement=True, comment='') #
    comment_pid                          = Column(VARCHAR(100), comment='') # 
    member_id                            = Column(VARCHAR(100), comment='') # 
    board_content_id                      = Column(VARCHAR(100), comment='') # 
    comment_body                         = Column(VARCHAR(1000), comment='') # 
    comment_regdatetime                      = Column(DATETIME, comment='') # 
    comment_edtdatetime                      = Column(DATETIME, comment='') # 
    comment_deleted                      = Column(VARCHAR(10), comment='') # 

    # autoincrement..
    # def __init__(self, commentId, **kwargs):
    #     self.comment_id = commentId
    def __init__(self, **kwargs):


        self.comment_pid                   = kwargs.get('comment_pid', None)
        self.member_id                     = kwargs.get('member_id', None)
        self.board_content_id              = kwargs.get('board_content_id', None)
        self.comment_body                  = kwargs.get('comment_body', None)
        self.comment_regdatetime           = kwargs.get('comment_regdatetime', None)
        self.comment_edtdatetime           = kwargs.get('comment_edtdatetime', None)
        self.comment_deleted               = kwargs.get('comment_deleted', None)

    def __repr__(self):
        return "{'comment_id' : '%s', \
        'comment_pid' : '%s', \
        'member_id' : '%s', \
        'board_content_id' : '%s', \
        'comment_body' : '%s', \
        'comment_regdatetime' : '%s', \
        'comment_edtdatetime' : '%s', \
        'comment_deleted' : '%s'}" % (
                    self.comment_id,
                    self.comment_pid,
                    self.member_id,
                    self.board_content_id,
                    self.comment_body,
                    self.comment_regdatetime,
                    self.comment_edtdatetime,
                    self.comment_deleted)
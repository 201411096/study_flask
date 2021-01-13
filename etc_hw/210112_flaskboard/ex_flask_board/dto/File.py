from sqlalchemy import Column, Integer, VARCHAR, NUMERIC, CHAR, DATETIME, TEXT
from __main__ import Base

class File(Base):
    __tablename__ = 'file' #파일 
    __table_args__ = {
            'comment' : '파일'
        }

    file_id                              = Column(VARCHAR(100), primary_key=True, comment='') # 
    board_content_id                      = Column(VARCHAR(100), comment='') # 
    member_id                            = Column(VARCHAR(100), comment='') # 
    file_name                            = Column(VARCHAR(100), comment='') # 
    file_path                            = Column(VARCHAR(100), comment='') # 
    file_type                            = Column(VARCHAR(100), comment='') # 
    file_regdatetime                      = Column(DATETIME, comment='') # 
    file_edtdatetime                      = Column(DATETIME, comment='') # 

    def __init__(self, fileId, **kwargs):
        self.file_id = fileId

        self.board_content_id              = kwargs.get('board_content_id', None)
        self.member_id                     = kwargs.get('member_id', None)
        self.file_name                     = kwargs.get('file_name', None)
        self.file_path                     = kwargs.get('file_path', None)
        self.file_type                     = kwargs.get('file_type', None)
        self.file_regdatetime              = kwargs.get('file_regdatetime', None)
        self.file_edtdatetime              = kwargs.get('file_edtdatetime', None)

    def __repr__(self):
        return "{'file_id' : '%s', \
        'board_content_id' : '%s', \
        'member_id' : '%s', \
        'file_name' : '%s', \
        'file_path' : '%s', \
        'file_type' : '%s', \
        'file_regdatetime' : '%s', \
        'file_edtdatetime' : '%s'}" % (
                    self.file_id,
                    self.board_content_id,
                    self.member_id,
                    self.file_name,
                    self.file_path,
                    self.file_type,
                    self.file_regdatetime,
                    self.file_edtdatetime)
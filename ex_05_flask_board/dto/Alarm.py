from sqlalchemy import Column, Integer, VARCHAR, NUMERIC, CHAR, DATETIME, TEXT, String
from __main__ import Base

class Alarm(Base):
    __tablename__ = 'alarm'

    from_member_id = Column(String(100))
    to_member_id = Column(String(100))
    alarm_content = Column(String(100))
    alarm_regdatetime = Column(String(100))
    alarm_id = Column(String(100), primary_key=True)
    alarm_target_content_id = Column(String(100))
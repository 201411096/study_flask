from __main__ import session
from dto import *
from sqlalchemy import exc, subquery, cast, text
from sqlalchemy import DateTime, Integer, String
from sqlalchemy.sql import bindparam
from util import *
import datetime

def comment_write(data):
    result = {}
    comment = Comment(
        comment_pid=data.get('comment_pid', None), member_id=data.get('member_id', None),
        board_content_id=data.get('board_content_id', None), comment_body=data.get('comment_body', None),
        comment_regdatetime=datetime.datetime.now(), comment_edtdatetime=datetime.datetime.now(), comment_deleted='N'
    )

    try:
        session.add(comment)
        session.commit()
        result['code'] = '1'
    except exc.IntegrityError:
        session.rollback()
        result['code'] = '0'
    return result
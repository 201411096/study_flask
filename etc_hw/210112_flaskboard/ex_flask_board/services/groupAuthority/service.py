from __main__ import session
from dto import *
from sqlalchemy import exc, subquery, cast, text
from sqlalchemy import DateTime, Integer, String
from sqlalchemy.sql import bindparam
from util import *
import datetime

def groupAuthority_getList(data):
    result = {}
    result = session.query(GroupAuthority).\
        with_entities(
            GroupAuthority.group_code, 
            GroupAuthority.authority_board_create,
            GroupAuthority.authority_board_update,
            GroupAuthority.authority_board_delete
        ).filter(GroupAuthority.group_code == data['group_code'])
    return queryToDict(result)
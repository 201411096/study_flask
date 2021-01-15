from __main__ import session
from dto import *
from sqlalchemy import exc
from util import *

def board_getList():
	resultData = session.query(BoardList).with_entities(BoardList.board_id, BoardList.board_name, BoardList.board_des)
	return queryToDict(resultData)

def board_write():
    return 1
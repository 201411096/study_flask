from __main__ import session
from dto import *
from sqlalchemy import exc, subquery, cast, text
from sqlalchemy import DateTime, Integer, String
from sqlalchemy.sql import bindparam
from util import *
import datetime

def board_getList():
	resultData = session.query(BoardList).with_entities(BoardList.board_id, BoardList.board_name, BoardList.board_des)
	return queryToDict(resultData)

def board_write(data):
	result = {}

	subq1 = session.query(Board)\
		.with_entities(Board.board_content_id)\
		.order_by(cast(Board.board_content_id, Integer).desc()).first()
	subq2 = session.query(Board)\
		.with_entities(Board.board_content_num)\
		.filter(Board.board_id == data['board_id'])\
		.order_by(cast(Board.board_content_num, Integer).desc()).first()

	# print('data1(board_write) : ', subq1)
	# print('data2(board_write) : ', subq2)
	# print('data1(board_write) : ', len(subq1))
	# print('data2(board_write) : ', len(subq2))
	# print('data1(board_write) : ', subq1.board_content_id)
	# print('data2(board_write) : ', subq2.board_content_num)
	if(subq1 is not None):
		bci = str(int(subq1.board_content_id)+1)
	else:
		bci = 1
	if(subq2 is not None):
		bcn = str(int(subq2.board_content_num)+1)
	else:
		bcn = 1

	board = Board(
		bci, board_content_pid = data.get('board_content_pid', None), member_id = data['member_id'],
		board_id = data['board_id'], board_content_title = data['board_content_title'], board_content_body=data['board_content_body'],
		board_content_regdatetime = datetime.datetime.now(), board_content_edtdatetime = datetime.datetime.now(),
		board_content_num = bcn, board_content_deleted='N'
	)
	try:
		session.add(board)
		session.commit()
		result['code'] = '1'
	except exc.IntegrityError:
		session.rollback()
		result['code'] = '0'
	return result

def board_contentList(data):
	query = """
	with recursive cte as
	(
	select  board_content_id,
			board_content_pid,
			member_id,
			board_content_title,
			board_content_body,
			board_content_regdatetime,
			board_content_edtdatetime,
			board_content_num,
			board_content_deleted,
			0 AS depth,
			CAST(LPAD(board_content_id, 10, "0") AS VARCHAR(1000)) as lvl
	from    board
	where   board_content_pid = 0 and board_id = :board_id
	union all
	select  r.board_content_id,
			r.board_content_pid,
			r.member_id,
			r.board_content_title,
			r.board_content_body,
			r.board_content_regdatetime,
			r.board_content_edtdatetime,
			r.board_content_num,
			r.board_content_deleted,
			depth + 1 AS depth,
			CONCAT(cte.lvl, "-", LPAD(r.board_content_id, 10, "0")) as lvl
	from    board r
	inner join cte
			on r.board_content_pid = cte.board_content_id
	)
	select * from cte
	ORDER BY lvl
	LIMIT :startrow, :numberInPage;
	"""
	statement = text(query)
	statement = statement.bindparams(
		bindparam("startrow", type_=Integer), 
		bindparam("numberInPage", type_=Integer),
		bindparam("board_id", type_=String))
	result = session.execute(statement, 
		{"startrow":  data["startrow"], 
		"numberInPage": data["numberInPage"],
		"board_id":data['board_id']})
	return queryToDict2(result)
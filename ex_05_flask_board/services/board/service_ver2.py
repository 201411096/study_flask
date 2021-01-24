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

    board = Board(
        board_content_pid = int(data.get('board_content_pid', None)), member_id = data['member_id'],
        board_id = data['board_id'], board_content_title = data['board_content_title'], board_content_body=data['board_content_body'],
        board_content_regdatetime = datetime.datetime.now(), board_content_edtdatetime = datetime.datetime.now(),
        board_content_deleted='N'
    )
    try:
        session.add(board)
        session.commit()
        result['code'] = '1'
    except exc.IntegrityError as e:
        print(e)
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
			board_content_deleted,
			0 AS depth,
			CAST(LPAD(board_content_id, 10, "0") AS VARCHAR(1000)) as grp,
			CAST(LPAD(board_content_id, 10, "0") AS VARCHAR(1000)) as lvl
	from    board
	where   board_content_pid = -1 and board_id = :board_id and board_content_deleted = 'N'
	union all
	select  r.board_content_id,
			r.board_content_pid,
			r.member_id,
			r.board_content_title,
			r.board_content_body,
			r.board_content_regdatetime,
			r.board_content_edtdatetime,
			r.board_content_deleted,
			depth + 1 AS depth,
			grp AS grp,
			CONCAT(cte.lvl, "-", LPAD(r.board_content_id, 10, "0")) as lvl
	from    board r
	inner join cte
			on r.board_content_pid = cte.board_content_id
	)
	SELECT * FROM
    (SELECT @ROWNUM:=@ROWNUM+1 AS board_content_num, c.* 
    FROM cte c, 
    (SELECT @ROWNUM:=0) b ORDER BY CAST(board_content_id AS INTEGER)) t 
    inner join member
    on t.member_id = member.member_id
    ORDER BY grp DESC, lvl
	LIMIT :startrow, :numberInPage
    ;
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
	
	result = queryToDict2(result)
	for row in result:
		for key in row.keys():
			if(type(row[key]) ==  datetime.datetime):
				row[key] = str(row[key])
	return result

def board_content(data):
	result = session.query(Board)\
			.join(Member, Member.member_id==Board.member_id)\
			.filter(Board.board_content_id==data['board_content_id'])\
			.with_entities(
				Board.board_content_id, Board.board_content_pid, Board.member_id,
				Board.board_content_title, Board.board_content_body, Board.board_content_regdatetime, Board.board_content_edtdatetime,
				Board.board_id, Board.board_content_num, Board.board_content_deleted,
				Member.member_nickname
			)
	print('type(board_content) : ', type(result))
	return queryToDict(result)

def board_update(data):
	resultData = {}
	data['board_content_edtdatetime'] = datetime.datetime.now()
	result = session.query(Board)\
			.filter(Board.board_content_id==data['board_content_id'])\
			.update(data, synchronize_session='fetch')
	
	session.commit()

	if result>=1:
		resultData['code']=1
	else:
		resultData['code']=0		
	return resultData

def board_delete(data):
	resultData = {}

	result = session.query(Board)\
			.filter(Board.board_content_id==data['board_content_id'])\
			.update({"board_content_deleted":"Y"}, synchronize_session='fetch')

	session.commit()

	if result>=1:
		resultData['code']=1
	else:
		resultData['code']=0
	return resultData
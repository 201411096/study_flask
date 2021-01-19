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
        comment_pid=data.get('comment_pid', 0), member_id=data.get('member_id', None),
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

def comment_contentList(data):
    query="""
	with recursive cte as
	(
	select  comment_id,
			comment_pid,
			member_id,
			board_content_id,
			comment_body,
			comment_regdatetime,
			comment_edtdatetime,
			comment_deleted,
			0 AS depth,
			CAST(LPAD(comment_id, 10, "0") AS VARCHAR(1000)) as grp,
			CAST(LPAD(comment_id, 10, "0") AS VARCHAR(1000)) as lvl
	from    comment
	where   comment_pid = 0 and board_content_id = :board_content_id
	union all
	select  r.comment_id,
			r.comment_pid,
			r.member_id,
			r.board_content_id,
			r.comment_body,
			r.comment_regdatetime,
			r.comment_edtdatetime,
			r.comment_deleted,
			depth + 1 AS depth,
			grp AS grp,
			CONCAT(cte.lvl, "-", LPAD(r.comment_id, 10, "0")) as lvl
	from    comment r
	inner join cte
			on r.comment_pid = cte.comment_id
	)
	select * from cte
	inner join member
	on cte.member_id = member.member_id
	ORDER BY grp desc, lvl
    """
    statement = text(query)
    statement = statement.bindparams(
        bindparam("board_content_id", type_=String)
    )
    result = session.execute(statement, 
		{"board_content_id":data['board_content_id']})
    print('210119 data : ', result)
    return queryToDict2(result)

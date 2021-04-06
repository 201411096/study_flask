from __main__ import session
from dto import *
from sqlalchemy import exc, subquery, cast, text, and_
from sqlalchemy import DateTime, Integer, String
from sqlalchemy.sql import bindparam
from util import *
import datetime
import uuid

def alarm_getList(data):
    result = None
    return result

def alarm_board_getMemberList(data):
    result = None

    initialRowSet = session.query(Board)\
                    .with_entities(
                        Board.board_content_id, Board.board_content_pid, Board.member_id,
                        Board.board_content_title, Board.board_content_body, 
                        Board.board_content_regdatetime, Board.board_content_edtdatetime,
                        Board.board_content_deleted
                    )\
                    .filter(and_(Board.board_content_id == data['board_content_id'], Board.board_id == data['board_id'], Board.board_content_deleted == 'N') )\
                    .cte(recursive=True)
    additionalRowSet = session.query(Board)\
                        .with_entities(
                            Board.board_content_id, Board.board_content_pid, Board.member_id,
                            Board.board_content_title, Board.board_content_body,
                            Board.board_content_regdatetime, Board.board_content_edtdatetime,
                            Board.board_content_deleted
                        )\
                        .join(initialRowSet, Board.board_content_id == initialRowSet.c.board_content_pid)
    recursiveRowSet = initialRowSet.union(additionalRowSet)

    resultData = session.query(recursiveRowSet)\
                .distinct(recursiveRowSet.c.member_id)\
                .with_entities(
                    recursiveRowSet.c.member_id,
                    Member.member_id
                )\
                .join(Member, Member.member_id == recursiveRowSet.c.member_id)
    result = queryToDict(resultData)
    # print('================ alarm_board_getMemberList ===============')
    # for row in result:
    #     print(row)
    # print('================ alarm_board_getMemberList ===============')
    return result
    
def alarm_board_send(data):
    result = {}
    alarm = Alarm(
        from_member_id = data['from_member_id'],
        to_member_id = data['to_member_id'],
        alarm_content = data['alarm_content'],
        alarm_regdatetime = datetime.datetime.now(),
        alarm_id = uuid.uuid4(),
        alarm_target_content_id = data['board_content_id']
    )

    try:
        session.add(alarm)
        session.commit()
        result['code'] = '1'
    except exc.IntegrityError as e:
        print(e)
        session.rollback()
        result['code'] = '0'
    return result

def alarm_read(data):
    result = {}
    
    resultData = session.query(Alarm)\
            .filter(and_(
                Alarm.alarm_target_content_id == data['board_content_id'],
                Alarm.to_member_id == data['to_member_id']
                ))\
            .delete()
    print('resultData 0208 : ', resultData)
    
    session.commit()
    result['code'] = '1'

    return result
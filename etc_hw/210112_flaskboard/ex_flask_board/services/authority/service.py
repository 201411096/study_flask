from __main__ import session
from dto import *
from sqlalchemy import exc, subquery, cast, text
from sqlalchemy import DateTime, Integer, String
from sqlalchemy.sql import bindparam
from util import *
import datetime

# 그룹권한
def authority_groupAuthority_getList(data):
    result = {}
    result = session.query(GroupAuthority)\
            .join(Member, Member.group_code==GroupAuthority.group_code)\
            .with_entities(
                Member.member_id,
                GroupAuthority.group_code, 
                GroupAuthority.authority_board_create,
                GroupAuthority.authority_board_update,
                GroupAuthority.authority_board_delete                
                ).filter(Member.member_id==data['member_id'])
    return queryToDict(result)

# 게시판권한
def authority_boardAuthority_getList(data):
    result = session.query(GroupBoardAuthority)\
        .join(Member, Member.group_code==GroupBoardAuthority.group_code)\
        .with_entities(
            Member.member_id,
            GroupBoardAuthority.group_code,
            GroupBoardAuthority.board_id,
            GroupBoardAuthority.authority_board_content_read,
            GroupBoardAuthority.authority_board_content_write,
            GroupBoardAuthority.authority_board_content_update,
            GroupBoardAuthority.authority_board_content_delete
        ).filter(Member.member_id==data['member_id'])
    rows = result.all()
    resultData = {}
    for row in rows:
        tempDict = row._asdict()
        # print(row)
        resultData[tempDict['board_id']]=tempDict
    return resultData

# 세션의 멤버아이디에 해당하는 권한을 가져옴
def getAuthorityList():
    data={}
    result = {}
    data['member_id'] = flaskSession.get('userData')['member_id']
    result['authority_group'] = authority_groupAuthority_getList(data)[0]
    result['authority_board'] = authority_boardAuthority_getList(data)
    return result
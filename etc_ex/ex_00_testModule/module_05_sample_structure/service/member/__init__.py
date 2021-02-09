from sqlalchemy import Column, VARCHAR, text, exc, and_, or_, func, String, DateTime
from database import getSession
from dto.model import *

def get_member(data):
    resultData = []

    rows = getSession()\
            .query(Member)\
            .with_entities(Member.member_id, Member.member_name)\
            .all()
    
    for row in rows:
        print(row)
        resultData.append(row)
    
    return resultData
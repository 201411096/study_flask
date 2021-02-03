# coding: utf-8
from sqlalchemy import create_engine, Column, DateTime, String, Integer, Table
from sqlalchemy import literal
from sqlalchemy.orm import aliased
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects.mysql import INTEGER
from sqlalchemy.ext.declarative import declarative_base

import os
import json

currentPath= os.path.dirname(os.path.abspath(__file__))
print(currentPath)
with open(currentPath+'/config.json', 'r') as f:
    dbconfig = json.load(f)
print(dbconfig)


SQLALCHEMY_DATABASE_URI = "mysql+mysqldb://{username}:{password}@{hostname}:{port}/{databasename}?charset=utf8".format(
    username=dbconfig['username'],
    password=dbconfig['password'],
    hostname=dbconfig['hostname'],
    port=dbconfig['port'],
    databasename=dbconfig['databasename']
)

DATABASES = create_engine(SQLALCHEMY_DATABASE_URI, echo = True)
Base = declarative_base()
metadata = Base.metadata

Session = sessionmaker()
Session.configure(bind=DATABASES)
session = Session()

class TestRecursive(Base):
    __tablename__ = 'test_recursive'

    id = Column(INTEGER(11), primary_key=True)
    pid = Column(INTEGER(11))
    nm = Column(String(20))

result = []
rows = None

# 단순쿼리 test
# rows = session.query(TestRecursive).with_entities(TestRecursive.id, TestRecursive.pid, TestRecursive.nm).all()



#initialRowSet
included_parts = session.query(TestRecursive)\
                    .with_entities(
                        TestRecursive.id, TestRecursive.pid, TestRecursive.nm,
                        literal(0, type_=Integer).label('depth')
                        )\
                    .filter(TestRecursive.id == 1)\
                    .cte(recursive=True)

incl_alias = aliased(included_parts) # cteName, name
parts_alias = aliased(TestRecursive)  # tableClassName, name

#initialRowSet, additionalRowSet
included_parts = incl_alias.union(
        session.query(parts_alias)\
            .with_entities(
                parts_alias.id, parts_alias.pid, parts_alias.nm,
                (incl_alias.c.depth+1).label('depth')
                )\
            .filter(parts_alias.pid == incl_alias.c.id)
    )

rows = session.query(included_parts)\
        .with_entities(
            included_parts.c.id, included_parts.c.pid, included_parts.c.nm,
            included_parts.c.depth
            ).all()
for row in rows:
    print(row)
    result.append(row._asdict())

print(result)

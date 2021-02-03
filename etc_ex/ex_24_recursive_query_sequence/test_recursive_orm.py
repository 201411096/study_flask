# coding: utf-8
from sqlalchemy import create_engine, Column, DateTime, VARCHAR, Integer, Table, String
from sqlalchemy import literal, func, cast, case
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

# cast(TestRecursive.id, String).label('grp') # 중간
#initialRowSet
included_parts = session.query(TestRecursive)\
                    .with_entities(
                        TestRecursive.id, TestRecursive.pid, TestRecursive.nm,
                        literal(0, type_=Integer).label('depth'),
                        case([
                            (func.length(cast(TestRecursive.id, VARCHAR(1000))) == 0, func.concat('0000000000', cast(TestRecursive.id, VARCHAR(1000)))),
                            (func.length(cast(TestRecursive.id, VARCHAR(1000))) == 1, func.concat('000000000', cast(TestRecursive.id, VARCHAR(1000)))),
                            (func.length(cast(TestRecursive.id, VARCHAR(1000))) == 2, func.concat('00000000', cast(TestRecursive.id, VARCHAR(1000)))),
                            (func.length(cast(TestRecursive.id, VARCHAR(1000))) == 3, func.concat('0000000', cast(TestRecursive.id, VARCHAR(1000)))),
                            (func.length(cast(TestRecursive.id, VARCHAR(1000))) == 4, func.concat('000000', cast(TestRecursive.id, VARCHAR(1000)))),
                            (func.length(cast(TestRecursive.id, VARCHAR(1000))) == 5, func.concat('00000', cast(TestRecursive.id, VARCHAR(1000)))),
                            (func.length(cast(TestRecursive.id, VARCHAR(1000))) == 6, func.concat('0000', cast(TestRecursive.id, VARCHAR(1000)))),
                            (func.length(cast(TestRecursive.id, VARCHAR(1000))) == 7, func.concat('000', cast(TestRecursive.id, VARCHAR(1000)))),
                            (func.length(cast(TestRecursive.id, VARCHAR(1000))) == 8, func.concat('00', cast(TestRecursive.id, VARCHAR(1000)))),
                            (func.length(cast(TestRecursive.id, VARCHAR(1000))) == 9, func.concat('0', cast(TestRecursive.id, VARCHAR(1000)))),
                            (func.length(cast(TestRecursive.id, VARCHAR(1000))) == 10, cast(TestRecursive.id, VARCHAR(1000)))
                        ]).label('grp'),
                        case([
                            (func.length(cast(TestRecursive.id, VARCHAR(1000))) == 0, func.concat('0000000000', cast(TestRecursive.id, VARCHAR(1000)))),
                            (func.length(cast(TestRecursive.id, VARCHAR(1000))) == 1, func.concat('000000000', cast(TestRecursive.id, VARCHAR(1000)))),
                            (func.length(cast(TestRecursive.id, VARCHAR(1000))) == 2, func.concat('00000000', cast(TestRecursive.id, VARCHAR(1000)))),
                            (func.length(cast(TestRecursive.id, VARCHAR(1000))) == 3, func.concat('0000000', cast(TestRecursive.id, VARCHAR(1000)))),
                            (func.length(cast(TestRecursive.id, VARCHAR(1000))) == 4, func.concat('000000', cast(TestRecursive.id, VARCHAR(1000)))),
                            (func.length(cast(TestRecursive.id, VARCHAR(1000))) == 5, func.concat('00000', cast(TestRecursive.id, VARCHAR(1000)))),
                            (func.length(cast(TestRecursive.id, VARCHAR(1000))) == 6, func.concat('0000', cast(TestRecursive.id, VARCHAR(1000)))),
                            (func.length(cast(TestRecursive.id, VARCHAR(1000))) == 7, func.concat('000', cast(TestRecursive.id, VARCHAR(1000)))),
                            (func.length(cast(TestRecursive.id, VARCHAR(1000))) == 8, func.concat('00', cast(TestRecursive.id, VARCHAR(1000)))),
                            (func.length(cast(TestRecursive.id, VARCHAR(1000))) == 9, func.concat('0', cast(TestRecursive.id, VARCHAR(1000)))),
                            (func.length(cast(TestRecursive.id, VARCHAR(1000))) == 10, cast(TestRecursive.id, VARCHAR(1000)))
                        ]).label('lvl')
                        )\
                    .filter(TestRecursive.pid == 0)\
                    .cte(recursive=True)

incl_alias = aliased(included_parts) # cteName, name
parts_alias = aliased(TestRecursive)  # tableClassName, name

#incl_alias.c.grp.label('grp'),
#initialRowSet, additionalRowSet

included_parts = incl_alias.union(
        session.query(parts_alias)\
            .with_entities(
                parts_alias.id, parts_alias.pid, parts_alias.nm,
                (incl_alias.c.depth+1).label('depth'),
                incl_alias.c.grp.label('grp'),
                func.concat(incl_alias.c.lvl, '-', case([
                    (func.length(cast(parts_alias.id, VARCHAR(1000))) == 0, func.concat('0000000000', cast(parts_alias.id, VARCHAR(1000)))),
                    (func.length(cast(parts_alias.id, VARCHAR(1000))) == 1, func.concat('000000000', cast(parts_alias.id, VARCHAR(1000)))),
                    (func.length(cast(parts_alias.id, VARCHAR(1000))) == 2, func.concat('00000000', cast(parts_alias.id, VARCHAR(1000)))),
                    (func.length(cast(parts_alias.id, VARCHAR(1000))) == 3, func.concat('0000000', cast(parts_alias.id, VARCHAR(1000)))),
                    (func.length(cast(parts_alias.id, VARCHAR(1000))) == 4, func.concat('000000', cast(parts_alias.id, VARCHAR(1000)))),
                    (func.length(cast(parts_alias.id, VARCHAR(1000))) == 5, func.concat('00000', cast(parts_alias.id, VARCHAR(1000)))),
                    (func.length(cast(parts_alias.id, VARCHAR(1000))) == 6, func.concat('0000', cast(parts_alias.id, VARCHAR(1000)))),
                    (func.length(cast(parts_alias.id, VARCHAR(1000))) == 7, func.concat('000', cast(parts_alias.id, VARCHAR(1000)))),
                    (func.length(cast(parts_alias.id, VARCHAR(1000))) == 8, func.concat('00', cast(parts_alias.id, VARCHAR(1000)))),
                    (func.length(cast(parts_alias.id, VARCHAR(1000))) == 9, func.concat('0', cast(parts_alias.id, VARCHAR(1000)))),
                    (func.length(cast(parts_alias.id, VARCHAR(1000))) == 10, cast(parts_alias.id, VARCHAR(1000)))                    
                ], else_= cast(parts_alias.id, VARCHAR(1000)) )).label('lvl'),
                )\
            .filter(parts_alias.pid == incl_alias.c.id)
    )

rows = session.query(included_parts)\
        .with_entities(
            included_parts.c.id, included_parts.c.pid, included_parts.c.nm,
            included_parts.c.depth,
            included_parts.c.grp,
            included_parts.c.lvl,
            ).all()
for row in rows:
    print(row)
    result.append(row._asdict())

print(result)

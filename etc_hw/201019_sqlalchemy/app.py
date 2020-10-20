from classFiles import *
from dataSource import session, insertData, insertAllData, selectData, deleteData, updateData, deleteData2, updateData2
from sqlalchemy import func
# data = Board.Board(100, writer_id=1000, title='title', content='abc')
# args = {'ab':'abb'}
# data = GOPntInfo.GOPntInfo(99999999)

# session.add(data)
# session.commit()
# insertData(data)

# print(session.query(GOPntInfo.GOPntInfo).filter()all())
# result = selectData(GOPntInfo.GOPntInfo)

# result = selectData(GOPntInfo.GOPntInfo, where='stn_id>100 and stn_id<120')
# result = selectData(GOPntInfo.GOPntInfo, where='stn_id>100 and stn_id<120', orderBy='stn_id desc')


# result = selectData(GOPntInfo.GOPntInfo, where='stn_id>100 and stn_id<120', orderBy='stn_id desc', type='list', withEntities=[GOPntInfo.GOPntInfo.stn_id, GOPntInfo.GOPntInfo.stn_ko])
# 집계함수 사용안함
result = selectData(GOPntInfo.GOPntInfo, where='stn_id>100 and stn_id<120', orderBy='stn_id desc', type='list', withEntities=[GOPntInfo.GOPntInfo.ht_wd], groupBy=[GOPntInfo.GOPntInfo.ht_wd], having='ht_wd>13')
# 집계함수 사용
# result = selectData(GOPntInfo.GOPntInfo, where='stn_id>100 and stn_id<120', orderBy='stn_id desc', type='list', withEntities=[GOPntInfo.GOPntInfo.ht_wd], groupBy=[GOPntInfo.GOPntInfo.ht_wd], having='ht_wd>13')

# result = selectData(GOPntInfo.GOPntInfo, where='stn_id>100 and stn_id<120', orderBy='stn_id desc', type='list', withEntities=['GOPntInfo.GOPntInfo.ht_wd'], groupBy=['GOPntInfo.GOPntInfo.ht_wd'], having='ht_wd>13')

print(result)

# print(deleteData(GOPntInfo.GOPntInfo, where='stn_id = 999999'))
# print(updateData(GOPntInfo.GOPntInfo, {'lat' : 4444, 'lon':44444, 'ht':4444 }, where='stn_id = 999999'))
# print(updateData2(GOPntInfo.GOPntInfo, {'lat' : 4444, 'lon':44444, 'ht':4444 }, where='stn_id > 99999'))
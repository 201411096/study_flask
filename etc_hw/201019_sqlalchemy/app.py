from classFiles import *
from dataSource import session, insertData, insertAllData, selectData, deleteData, updateData

# data = Board.Board(100, writer_id=1000, title='title', content='abc')

# session.add(data)
# session.commit()

# insertData(data)

# print(session.query(GOPntInfo.GOPntInfo).filter()all())
# result = selectData(GOPntInfo.GOPntInfo)

# result = selectData(GOPntInfo.GOPntInfo, where='stn_id>100 and stn_id<120')
# result = selectData(GOPntInfo.GOPntInfo, where='stn_id>100 and stn_id<120', orderBy='stn_id desc')

# result = selectData(GOPntInfo.GOPntInfo, where='stn_id>100 and stn_id<120', orderBy='stn_id desc', type='query')

# print(result.all())

deleteData(GOPntInfo.GOPntInfo, where='stn_id = 999999')
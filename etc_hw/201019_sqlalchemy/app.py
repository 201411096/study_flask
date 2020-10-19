from ClassFiles import *
from dataSource import session

data = Board.Board(100, writer_id=1000, title='title', content='abc')

session.add(data)
session.commit()
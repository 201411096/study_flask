from dataSource import *
class Board(Base):
	__tablename__ = 'board' # 
	__table_args__ = {
			'comment' : ''
		}

	id              					 = Column(Integer, primary_key=True, comment='') # 
	writer_id       					 = Column(VARCHAR(64), comment='') # 
	title           					 = Column(VARCHAR(128), comment='') # 
	content         					 = Column(TEXT, comment='') # 

	def __init__(self, id, **kwargs):
		self.id = id

		self.writer_id                     = kwargs.get('writer_id', None)
		self.title                         = kwargs.get('title', None)
		self.content                       = kwargs.get('content', None)

	def __repr__(self):
		return "{'id' : %s, \
		'writer_id' : %s, \
		'title' : %s, \
		'content' : %s}" % (
					self.id,
					self.writer_id,
					self.title,
					self.content)
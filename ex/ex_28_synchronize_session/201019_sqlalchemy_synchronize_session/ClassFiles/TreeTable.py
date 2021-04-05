from dataSource import *
class TreeTable(Base):
	__tablename__ = 'tree_table' # 
	__table_args__ = {
			'comment' : ''
		}

	id              					 = Column(Integer, primary_key=True, comment='') # 
	pid             					 = Column(Integer, comment='') # 
	NAME            					 = Column(VARCHAR(20), comment='') # 
	description     					 = Column(VARCHAR(500), comment='') # 

	def __init__(self, id, **kwargs):
		self.id = id

		self.pid                           = kwargs.get('pid', None)
		self.NAME                          = kwargs.get('NAME', None)
		self.description                   = kwargs.get('description', None)

	def __repr__(self):
		return "{'id' : %s, \
		'pid' : %s, \
		'NAME' : %s, \
		'description' : %s}" % (
					self.id,
					self.pid,
					self.NAME,
					self.description)
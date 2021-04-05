from dataSource import *
class Emp(Base):
	__tablename__ = 'emp' # 
	__table_args__ = {
			'comment' : ''
		}

	id              					 = Column(Integer, primary_key=True, comment='') # 
	name            					 = Column(VARCHAR(128), comment='') # 
	gender          					 = Column(VARCHAR(16), comment='') # 
	age             					 = Column(Integer, comment='') # 
	location        					 = Column(VARCHAR(32), comment='') # 
	deptno          					 = Column(Integer, comment='') # 
	hiredate        					 = Column(DATETIME, comment='') # 
	salary          					 = Column(Integer, comment='') # 

	def __init__(self, id, **kwargs):
		self.id = id

		self.name                          = kwargs.get('name', None)
		self.gender                        = kwargs.get('gender', None)
		self.age                           = kwargs.get('age', None)
		self.location                      = kwargs.get('location', None)
		self.deptno                        = kwargs.get('deptno', None)
		self.hiredate                      = kwargs.get('hiredate', None)
		self.salary                        = kwargs.get('salary', None)

	def __repr__(self):
		return "{'id' : %s, \
		'name' : %s, \
		'gender' : %s, \
		'age' : %s, \
		'location' : %s, \
		'deptno' : %s, \
		'hiredate' : %s, \
		'salary' : %s}" % (
					self.id,
					self.name,
					self.gender,
					self.age,
					self.location,
					self.deptno,
					self.hiredate,
					self.salary)
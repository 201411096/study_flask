from sqlalchemy.orm import aliased
from sqlalchemy import Column, ForeignKey, Integer, Table, Text
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite://', echo=True)
Session = sessionmaker(bind=engine)

session = Session()

Base = declarative_base()

association_table = Table('association_table', Base.metadata,
                           Column('parent_id', Integer, ForeignKey('node.id'), primary_key=True),
                           Column('child_id', Integer, ForeignKey('node.id'), primary_key=True))


class Node(Base):
    __tablename__ = 'node'
    id = Column(Integer, primary_key=True)
    property_1 = Column(Text)
    property_2 = Column(Integer)

    # http://docs.sqlalchemy.org/en/latest/orm/join_conditions.html#self-referential-many-to-many-relationship
    child = relationship('Node',
                            secondary=association_table,
                            primaryjoin=id==association_table.c.parent_id,
                            secondaryjoin=id==association_table.c.child_id,
                            backref='parent'
                            )

    def descendant_nodes(self):
        nodealias = aliased(Node)
        descendants = session.query(Node.id, Node.property_1, (self.property_1 + '/' + Node.property_1).label('path')).filter(Node.parent.contains(self))\
            .cte(recursive=True)
        descendants = descendants.union(
            session.query(nodealias.id, nodealias.property_1, (descendants.c.path + '/' + nodealias.property_1).label('path')).join(descendants, nodealias.parent)
        )
        return session.query(descendants.c.property_1, descendants.c.path).all()


Base.metadata.create_all(engine)

a = Node(property_1='a', property_2=1)
b = Node(property_1='b', property_2=2)
c = Node(property_1='c', property_2=3)
d = Node(property_1='d', property_2=4)
e = Node(property_1='e', property_2=5)
f = Node(property_1='f', property_2=6)
g = Node(property_1='g', property_2=7)
h = Node(property_1='h', property_2=8)
i = Node(property_1='i', property_2=9)



session.add_all([a, b, c, d, e, f, g, h, i])
a.child.append(d)
b.child.append(d)
d.child.append(g)
d.child.append(h)
g.child.append(i)
b.child.append(e)
e.child.append(h)
c.child.append(f)
e.child.append(i)

session.commit()


for item in b.descendant_nodes():
    print(item)

session.close()


"""
Graph should be setup like this:

a   b    c
 \ / \   |
  d   e  f
  |\ /|
  g h |    
  +---+
  i

"""
"""
output
('d', 'b/d')
('e', 'b/e')
('g', 'b/d/g')
('h', 'b/d/h')
('h', 'b/e/h')
('i', 'b/e/i')
('i', 'b/d/g/i')
"""
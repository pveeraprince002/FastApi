from sqlalchemy import Column,Integer,String
from database import base

class User(base):
    __tablename__='User'

    id =  Column(Integer, primary_key=True)
    name = Column(String)
    mobile=Column(String)

    def __repr__(self):
        return "<User(name=name'%s', mobile='%s')>" % (self.name,self.mobile)
    


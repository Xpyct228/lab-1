from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine,ForeignKey
from sqlalchemy.orm import Session
from sqlalchemy.dialects.mssql import BIT,DATETIME

Base = declarative_base()
metadata = Base.metadata
class User(Base):
   __tablename__ = 'User'

   id = Column(Integer,primary_key=True)
   username = Column(String)
   firstName = Column(String)
   lastName = Column(String)
   email = Column(String)
   password = Column(String)
   phone = Column(String)
   userRole=Column(Integer)
##   karma = Column(Integer)
class Med(Base):
   __tablename__ = 'Med'

   id = Column(Integer,primary_key=True)
   name = Column(String)
   price = Column(Integer)
   number = Column(String)
   photoUrl = Column(String)
   description = Column(String)
   demand = Column(BIT)
   
class Order(Base):
   __tablename__ = 'Order'

   id = Column(Integer,primary_key=True)
   userId  = Column(Integer,ForeignKey("User.id"))
   medId  = Column(Integer,ForeignKey("Med.id"))
   quantity = Column(Integer)
   status = Column(String)
   date = Column(DATETIME)
   
engine = create_engine('mssql+pyodbc://PC0007/lab-2?driver=SQL+Server+Native+Client+11.0')

Base.metadata.create_all(engine)
##
##session.add(User(username="yurko",
##                 firstName="yuri",
##                 lastName="kryvenchuk",
##                 email="yurkO@lpnu",
##                 password="14881488",
##                 phone="15621562",
##                 userRole=3))
##session.commit()
print(User.__table__)

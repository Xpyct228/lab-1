from sqlalchemy import Column, Integer, String
import mysql.connector
from mysql.connector import connect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.orm import Session
from sqlalchemy.dialects.mssql import  DATETIME
from werkzeug.security import generate_password_hash
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
Base = declarative_base()
metadata = Base.metadata

class User(Base):
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    username = Column(String(100), index=True)
    firstName = Column(String(100), index=True)
    lastName = Column(String(100), index=True)
    password = Column(String(100), index=True)
    phone = Column(String(100), index=True)
    userRole = Column(String(100), index=True)

    def __init__(self, username, firstName, lastName, password, phone, userRole):
        self.username = username
        self.firstName = firstName
        self.lastName = lastName

        self.password = password
        self.phone = phone
        self.userRole = userRole

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

##   karma = Column(Integer)
class Med(Base):
    __tablename__ = 'Med'

    id = Column(Integer, primary_key=True)
    name = Column(String(16), index=True)
    price = Column(Integer)
    number = Column(Integer)
    photoUrl = Column(String(16), index=True)
    description = Column(String(16), index=True)
    demannd=Column(String(16), index=True)
    def __init__(self, name, price, number , photoUrl, description,demannd):
        self.name = name
        self.price = price
        self.number  = number
        self.photoUrl = photoUrl
        self.description = description
        self.demannd=demannd

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
class Upd(Base):
        __tablename__ = 'Upd'

        id = Column(Integer, primary_key=True)
        id_medicine= Column(Integer, primary_key=True)
        new_price = Column(Integer)
        new_number = Column(String(16), index=True)


        def __init__(self,id_medicine, new_price, new_number):

            self.id_medicine = id_medicine
            self.new_price = new_price
            self.new_number = new_number


        def as_dict(self):
            return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class Order(Base):
    __tablename__ = 'Order'

    id = Column(Integer, primary_key=True)
    userId = Column(Integer, ForeignKey("User.id"))
    medId = Column(Integer, ForeignKey("Med.id"))
    quantity = Column(Integer)
    status = Column(String(16), index=True)
    date = Column(DATETIME)

    def __init__(self, userId, medId, quantity, status,date):
        self.userId = userId
        self.medId= medId
        self.quantity = quantity
        self.status = status

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.colum}


engine = create_engine('mysql+mysqlconnector://root:romik4252@localhost:3306/db_lab6')
Base.metadata.create_all(engine)

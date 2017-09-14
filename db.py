#coding:utf-8
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer,Float,ForeignKey
from sqlalchemy import and_,or_
from sqlalchemy.orm import sessionmaker
USER_NAME = "web"
PASSWORD = "web"
HOST = "localhost"
DATABASE = "d"
DB_URI = "mysql://{}:{}@{}/{}".format(USER_NAME,PASSWORD,HOST,DATABASE)
engine = create_engine(DB_URI)
Base = declarative_base()
class User(Base):
    __tablename__ = "user"
    id =Column(Integer,primary_key = True,autoincrement = True)
    name = Column(String(50))
    password = Column(String(100))
    areacode = Column(Integer)
    #total means consumption
    total = Column(Float)
    #cur total means current consumption
    cur_total = Column(Float)
class Commodit(Base):
    __tablename__ = "commodit"
    points = Column(Float)
    id = Column(Integer,primary_key = True,autoincrement = True)
    name = Column(String(50))
    amounts = Column(Integer)
    price = Column(Float)
    vol = Column(Integer)
    img_src = Column(String(1000))
class userlikes(Base):
    __tablename__ = "userlikes"
    id = 

    


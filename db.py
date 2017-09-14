#coding:utf-8
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer,Float,ForeignKey
from sqlalchemy import PrimaryKeyConstraint
from sqlalchemy import and_,or_
from sqlalchemy.orm import sessionmaker,relationship

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
class Userlikes(Base):
    __tablename__ = "userlikes"
    __table_args__ =    (PrimaryKeyConstraint("commodit_id","user_id"),)
    commodit_id = Column(Integer,ForeignKey("commodit.id"))
    user_id = Column(Integer,ForeignKey("user.id"))
    #relevant
    user = relationship("User",back_populates = "userlikes")
    commodit = relationship("Commodit",back_populates = "userlikes")


    vol = Column(Float)
class Order_s(Base):
    __tablename__ = "order_sum"
    order_id = Column(Integer,primary_key = True,autoincrement = True)
    total = Column(Float)
    user_id = Column(Integer,ForeignKey("user.id"))
    #relevant
    user = relationship("User",back_populates = "order_sum")
    order_type = Column(Integer)
class Order(Base):
    __tablename__ = "orderinfo"
    __table_args__ = (PrimaryKeyConstraint("order_id","commodit_id"),)
    order_id = Column(Integer,ForeignKey("order_sum.id"))
    commodit_id = Column(Integer,ForeignKey("commodit.id"))
    user_id = Column(Integer)
    amounts = Column(Integer)
    #relevant
    order_sum = relationship("Order_s",back_populates = "orderinfo")
    commodit = relationship("Commodit",back_populates = "orderinfo")
Order_s.orderinfo = relationship("Order",order_by = Order.commodit_id,back_populates = "oder_sum")


    


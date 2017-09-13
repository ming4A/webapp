from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer,Float
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


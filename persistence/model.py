from sqlalchemy import Column
from sqlalchemy import String,Integer
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Auth_user(Base):
	__tablename__ = 'auth_user'
	id = Column(Integer, primary_key=True,autoincrement=True)
	username = Column(String(150))
	password = Column(String(128))	
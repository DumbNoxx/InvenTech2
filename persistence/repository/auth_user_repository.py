import sqlalchemy as db
from persistence.model import Auth_user,Inventary
from sqlalchemy.orm import Session


class AuthUserRepository():

	def __init__(self):
		self.engine = db.create_engine('sqlite:///db/login.sqlite',echo=False,future=True)

	def getUserByUserName(self,user_name:str):
		user:Auth_user = None
		with Session(self.engine) as session:
			user = session.query(Auth_user).filter_by(username=user_name).first()

		return user


	def insertUser(self,user:Auth_user):
		with Session(self.engine) as session:
			session.add(user)
			session.commit()

	def insertProduct(self,name_products:Inventary):
		with Session(self.engine) as session:
			session.add(name_products)
			session.commit()

	def getProductInInventary(self,name_products:str):
		name:Inventary = None
		with Session(self.engine) as session:
			name = session.query(Inventary).filter_by(name_product=name).first()

		return name
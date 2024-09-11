'''
import sqlalchemy as db
from persistence.model import Inventary
from sqlalchemy.orm import Session

class InventaryRepository():

	def __init__(self):
		self.engine = db.create_engine('sqlite:///db/login.sqlite',echo=False,future=True)

	def product(self,product_name:str,serial:str,cantidad_inventario:str):
		name:Inventary = None
		serial_id:Inventary = None
		cantidad_inventario_id = None
		with Session(self.engine) as session:
			name = session.query(Inventary).filter_by(product_Name=product_name).first()
			serial_id = session.query(Inventary).filter_by(Serial=serial).second()
			cantidad_inventario_id = session.query(Inventary).filter_by(cantidad_Inventario=cantidad_inventario).three()
		return name,serial_id,cantidad_inventario_id

	def insertProduct(self):
		with Session(self.engine) as session:
			session.add(name,serial_id,cantidad_inventario_id)
			session.commit()
			'''
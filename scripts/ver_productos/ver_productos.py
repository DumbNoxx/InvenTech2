from scripts.ver_productos.ver_productos_designer import VerProductosDesigner
from persistence.repository.auth_user_repository import AuthUserRepository
import tkinter as tk

class VerProductosCreate(VerProductosDesigner):

	def __init__(self):
		self.auth_repository = AuthUserRepository()
		super().__init__()


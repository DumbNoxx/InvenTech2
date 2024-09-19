from scripts.ver_productos.ver_productos_designer import VerProductosDesigner
from persistence.repository.auth_user_repository import AuthUserRepository
from persistence.model import Inventary
import tkinter as tk
from tkinter import ttk
from sqlalchemy.orm import Session
import sqlalchemy as db
from tkinter import messagebox

class VerProductosCreate(VerProductosDesigner):

	def __init__(self):
		self.auth_repository = AuthUserRepository()
		super().__init__()


	def Buscar(self):
		if self.entrada_principal.get() == '':
			messagebox.showerror(message='El campo esta vacio, no se puedo buscar a la nada',title='Error')
		else:
			prod:Inventary = self.auth_repository.SearchInInventary(self.entrada_principal.get())
			if (self.InInventary(prod)):
				messagebox.showinfo(message=f'Producto {self.entrada_principal.get()} encontrado.')			


	def InInventary(self,inventario:Inventary):
		status:bool = True
		if (inventario == None):
			status = False
			messagebox.showinfo(message=f'Producto {self.entrada_principal.get()} no encontrado')
		return status
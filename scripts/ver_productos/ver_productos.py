from scripts.ver_productos.ver_productos_designer import VerProductosDesigner
from persistence.repository.auth_user_repository import AuthUserRepository
from persistence.model import Inventary
import tkinter as tk
from tkinter import ttk
from sqlalchemy.orm import Session
import sqlalchemy as db
from tkinter import messagebox
from util.barra_progreso import BarraProgresiva

class VerProductosCreate(VerProductosDesigner):

	def __init__(self):
		self.auth_repository = AuthUserRepository()
		super().__init__()


	def Buscar(self):
		if self.entrada_principal.get() == '':
			BarraProgresiva()
			self.auth_repository = AuthUserRepository()
			prod:Inventary = self.auth_repository.getProductInInventary()
			elen = self.tree.get_children()

			for element in elen:
				self.tree.delete(element)
			
			for prods in prod:
				self.tree.insert('',tk.END,text=prods.id,value=(prods.name_product,f'{prods.inventary_product} unidades',f'{prods.price_product}$'))
		else:
			elen = self.tree.get_children()
			products = self.auth_repository.SearchInInventary(self.entrada_principal.get())
			self.entrada_principal.delete(0,tk.END)

			for element in elen:
				self.tree.delete(element)
			
			for produt in products:
				self.tree.insert('',tk.END,text=produt.id,value=(produt.name_product,f'{produt.inventary_product} unidades',f'{produt.price_product}$'))


	def InInventary(self,inventario:Inventary):
		status:bool = True
		if (inventario == None):
			status = False
			messagebox.showinfo(message=f'Producto "{self.entrada_principal.get()}" no encontrado')
		return status

	def leave(self):
			resultado = messagebox.askquestion("Salir", '¿Estás seguro qué deseas salir de la ventana?', icon='question', default='no')
			if resultado == 'yes':
				self.ventana.destroy()
from scripts.agregar_producto.agregar_producto_designer import AgregarProductoDesigner
from persistence.repository.auth_user_repository import AuthUserRepository
from persistence.model import Inventary
from tkinter import messagebox
import tkinter as tk

class AgregarProductoCreate(AgregarProductoDesigner):

	def __init__(self):
		self.auth_repository = AuthUserRepository()
		super().__init__()

	def Add(self):
		add = Inventary()
		if self.nombre_producto.get() == '' and self.serial_producto.get() == '' and self.cantidad_producto.get() == '' and self.precio_producto.get() == '':
			messagebox.showerror(
				message='Los campos estan vacios, por favor completarlos',title='Error')
		elif self.nombre_producto.get() == '' or self.serial_producto.get() == '':
			messagebox.showerror(
				message='Hay campos vacios, por favor completar los campos',title='Error')
		elif self.cantidad_producto.get() == "" or self.precio_producto.get() == "":
			messagebox.showerror(
				message='Hay campos vacios, por favor completar los campos',title='Error')
		else:
			add.name_product = self.nombre_producto.get()
			add.serial_product = self.serial_producto.get()
			add.inventary_product = self.cantidad_producto.get()
			add.price_product = self.precio_producto.get()
			self.auth_repository.insertProduct(add)
			messagebox.showinfo(
					message=f'Producto "{self.nombre_producto.get()}" agregado satisfactoriamente',title='Agregar Producto')
			self.nombre_producto.delete(0,'end')
			self.serial_producto.delete(0,'end')
			self.cantidad_producto.delete(0,'end')
			self.precio_producto.delete(0,'end')
		
	def leave(self):
			resultado = messagebox.askquestion("Salir", '¿Estás seguro qué deseas salir de la ventana?', icon='question', default='no')
			if resultado == 'yes':
				self.ventana.destroy()


if __name__ == '__main__':
	AgregarProductoCreate()
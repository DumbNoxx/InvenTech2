#!/usr/bin/env python3
from scripts.facturar_producto.facturar_producto_designer import FacturarProductDesginer
from persistence.repository.auth_user_repository import AuthUserRepository
import tkinter as tk
from tkinter import messagebox

class FacturarProductCreate(FacturarProductDesginer):
	def __init__(self):
		self.auth_repository = AuthUserRepository()
		super().__init__()

	def leave(self):
		resultado = messagebox.askquestion("Salir", '¿Estás seguro qué deseas salir de la ventana?', icon='question', default='no')
		if resultado == 'yes':
			self.ventana.destroy()

	def facturar(self):
		if self.entrada.get() == '' and self.entrada2.get() == '':
			messagebox.showerror('Error','Los campos estan vacios.')
		elif self.entrada.get()== '' or self.entrada2.get() == '':
			messagebox.showerror('Error','Algun campo esta vacio.')
		else:
			print('Funciona')


if __name__ == '__main__':
	FacturarProductCreate()
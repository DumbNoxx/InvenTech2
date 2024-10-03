#!/usr/bin/env python3
from scripts.facturar_producto.facturar_producto_designer import FacturarProductDesginer
import tkinter as tk
from tkinter import messagebox

class FacturarProductCreate(FacturarProductDesginer):
	def __init__(self):
		super().__init__()

	def leave(self):
		resultado = messagebox.askquestion("Salir", '¿Estás seguro qué deseas salir de la ventana?', icon='question', default='no')
		if resultado == 'yes':
			self.ventana.destroy()

if __name__ == '__main__':
	FacturarProductCreate()
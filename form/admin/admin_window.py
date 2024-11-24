#!usr/bin/env python3

from form.admin.admin_window_designer import AdminWindowDesigner
from tkinter import messagebox
import main

class AdminWindow(AdminWindowDesigner):

	def __init__(self):
		super().__init__()

	def leave(self):
		resultado = messagebox.askquestion('Salir','¿Estás seguro qué deseas salir?', icon='question', default='no')
		if resultado == 'yes':
			self.ventana.destroy()
			main.PantallaCarga()
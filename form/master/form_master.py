#!/usr/bin/env python3

import tkinter as tk
from tkinter.font import BOLD
import util.generic as util
import os
from scripts.calculadora.calculadora import CalculadoraCreate
from scripts.agregar_producto.agregar_producto import AgregarProductoCreate
from scripts.ver_productos.ver_productos import VerProductosCreate
import main
import subprocess
from persistence.repository.auth_user_repository import AuthUserRepository
from persistence.model import Auth_user
from tkinter import messagebox


class MasterPanel:
	def __init__(self):
		self.auth_repository = AuthUserRepository()

		self.ventana = tk.Tk()
		self.ventana.title('InvenTech')
		w,h = self.ventana.winfo_screenwidth(),self.ventana.winfo_screenheight()
		util.centrar_ventana(self.ventana,1200,700)
		self.ventana.config(bg='#09ab53')
		icon_1 = tk.PhotoImage(file='./resources/icons.ico')

	

		logo = util.leer_image('./resources/logotipo.png',(350,350))

		label1 = tk.Label(self.ventana,image=logo,bg='#1abc9c')
		label1.place(relx=0,rely=0,relwidth=1,relheight=1)

		copyrigth = tk.Label(self.ventana,text='Nox Corporations ©',width=40,padx=6,pady=6,bg='#1abc9c',font=('Dyuthi',10))
		copyrigth.place(relx=0.90,rely=0.80,relwidth=0.10,relheight=0.10)

		label_title = tk.Label(self.ventana,text='InvenTech',bg='#1abc9c',font=('Dyuthi',36),fg='#f4d03f')
		label_title.place(relx=0.40,rely=0,relwidth=0.20,relheight=0.10)

		label_description = tk.Label(self.ventana,text='Sistema de Inventario',bg='#1abc9c',font=('Dyuthi',18),fg='#f4d03f')
		label_description.place(relx=0.40,rely=0.08,relwidth=0.20,relheight=0.05)


		def calcu():
			CalculadoraCreate()

		boton = tk.Button(self.ventana,text='Calculadora',bg='#a3e4d7',font=('Dyuthi',12),fg='black',command=calcu)
		boton.place(relx=0.45,rely=0.23,relwidth=0.09,relheight=0.07)

		def product():
			AgregarProductoCreate()

		boton1 = tk.Button(self.ventana,text='Agregar Producto',bg='#a3e4d7',font=('Dyuthi',12),fg='black',command=product)
		boton1.place(relx=0.30,rely=0.28,relwidth=0.11,relheight=0.07)

		def verProduct():
			VerProductosCreate()

		boton2 = tk.Button(self.ventana,text='Ver lista de productos',bg='#a3e4d7',font=('Dyuthi',12),fg='black',command=verProduct)
		boton2.place(relx=0.26,rely=0.40,relwidth=0.13,relheight=0.07)

		def leave():
			resultado = messagebox.askquestion("Salir", '¿Estás seguro que quieres cerrar sesión?', icon='question', default='no')
			if resultado == 'yes':
				self.ventana.destroy()
				main.PantallaCarga()

		cerrar_sesion = tk.Button(self.ventana,text='Cerrar Sesion',bg='#a3e4d7',font=('Dyuthi',12),fg='black',command=leave)
		cerrar_sesion.place(relx=0.01,rely=0.80,relwidth=0.09,relheight=0.07)


		self.ventana.iconphoto(True,icon_1)
		self.ventana.mainloop()
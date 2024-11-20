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
		self.ventana.geometry("%dx%d+0+0" % (w,h))
		self.ventana.config(bg='#09ab53')
		self.ventana.resizable(width=0,height=0)
		icon_1 = tk.PhotoImage(file='./resources/icons.ico')

	

		logo = util.leer_image('./resources/logotipo.png',(350,350))

		label1 = tk.Label(self.ventana,image=logo,bg='#1abc9c')
		label1.place(x=0,y=0,relwidth=1,relheight=1)

		copyrigth = tk.Label(self.ventana,text='Nox Corporations ©',width=40,padx=6,pady=6,bg='#1abc9c',font=('Dyuthi',10))
		copyrigth.place(x=1200,y=600,relwidth=0.10,relheight=0.10)

		label_title = tk.Label(self.ventana,text='InvenTech',bg='#1abc9c',font=('Dyuthi',36),fg='#f4d03f')
		label_title.place(x=70,y=40,relwidth=0.9,relheight=0.05)
		label_description = tk.Label(self.ventana,text='Sistema de Inventario',bg='#1abc9c',font=('Dyuthi',18),fg='#f4d03f')
		label_description.place(x=70,y=90,relwidth=0.9,relheight=0.03)


		def calcu():
			CalculadoraCreate()

		boton = tk.Button(self.ventana,text='Calculadora',bg='#a3e4d7',font=('Dyuthi',12),fg='black',command=calcu)
		boton.place(x=620,y=170,relwidth=0.09,relheight=0.07)

		def product():
			AgregarProductoCreate()

		boton1 = tk.Button(self.ventana,text='Agregar Producto',bg='#a3e4d7',font=('Dyuthi',12),fg='black',command=product)
		boton1.place(x=450,y=200,relwidth=0.09,relheight=0.07)

		def verProduct():
			VerProductosCreate()

		boton2 = tk.Button(self.ventana,text='Ver lista de productos',bg='#a3e4d7',font=('Dyuthi',12),fg='black',command=verProduct)
		boton2.place(x=400,y=300,relwidth=0.11,relheight=0.07)

		def juegos():
			pass
		#Titulo del boton: Facturar Producto
		boton3 = tk.Button(self.ventana,text='Ni idea',bg='#a3e4d7',font=('Dyuthi',12),fg='black',command=juegos)
		boton3.place(x=780,y=200,relwidth=0.11,relheight=0.07)

		def leave():
			resultado = messagebox.askquestion("Salir", '¿Estás seguro que quieres cerrar sesión?', icon='question', default='no')
			if resultado == 'yes':
				self.ventana.destroy()
				main.PantallaCarga()

		cerrar_sesion = tk.Button(self.ventana,text='Cerrar Sesion',bg='#a3e4d7',font=('Dyuthi',12),fg='black',command=leave)
		cerrar_sesion.place(x=10,y=600,relwidth=0.09,relheight=0.07)


		self.ventana.iconphoto(True,icon_1)
		self.ventana.mainloop()
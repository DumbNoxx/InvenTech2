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
import customtkinter as ct
from PIL import Image
import time


class MasterPanel:
	def __init__(self):
		self.auth_repository = AuthUserRepository()

		self.ventana = tk.Tk()
		self.ventana.title('InvenTech')
		util.centrar_ventana(self.ventana,1200,700)
		self.ventana.config(bg='#222831')
		icon_1 = tk.PhotoImage(file='./resources/icons.ico')

		my_image = ct.CTkImage(light_image=Image.open("./resources/Icono_Rework.png"),
			dark_image=Image.open("./resources/Icono_Rework.png"),
			size=(340,180))

		frame_principal = ct.CTkFrame(self.ventana,fg_color='#222831')
		frame_principal.pack(side='top',fill=tk.BOTH,expand=tk.YES)

		frame_left = ct.CTkFrame(frame_principal, width=300,height=700,fg_color='#31363F')
		frame_left.pack(side='left')

		copyrigth = ct.CTkLabel(frame_left,text='Nox Corporations ©',font=('Dyuthi',14),text_color='#EEEEEE',fg_color='#31363F')
		copyrigth.place(relx=0.18,rely=0.86,relwidth=0.38,relheight=0.20)

		label_title = ct.CTkLabel(frame_principal,text='InvenTech',fg_color='transparent',font=('Dyuthi',36),text_color='#EEEEEE')
		label_title.place(relx=0.40,rely=0.02,relwidth=0.20,relheight=0.07)

		label_title_frame = ct.CTkLabel(frame_left,text=f'Bienvenido',fg_color='transparent',font=('Dyuthi',36),text_color="#EEEEEE")
		label_title_frame.place(relx=0.10,rely=0.05,relwidth=0.80,relheight=0.10)

		frame_menu = ct.CTkFrame(frame_left,width=400,height=400,fg_color='#222831')
		frame_menu.place(relx=0.20,rely=0.19,relwidth=0.60,relheight=0.40)

		label_menu = ct.CTkLabel(frame_left,text='Menu',fg_color='transparent',font=('Dyuthi',16),text_color='#EEEEEE')
		label_menu.place(relx=0.28,rely=0.15,relwidth=0.40,relheight=0.03)
	
		def calcu():
			CalculadoraCreate()

		boton = ct.CTkButton(frame_menu,text="Calculadora", fg_color="transparent", hover=False, text_color="#76ABAE",command=calcu)
		boton.configure(border_width=0, cursor="hand2")
		boton.place(relx=0.16,rely=0.12,relwidth=0.60,relheight=0.08)

		def product():
			AgregarProductoCreate()

		boton1 = ct.CTkButton(frame_menu,text="Agregar Producto", fg_color="transparent", hover=False, text_color="#76ABAE",command=product)
		boton1.configure(border_width=0, cursor="hand2")
		boton1.place(relx=0.14,rely=0.25,relwidth=0.66,relheight=0.10)

		def verProduct():
			VerProductosCreate()

		boton2 = ct.CTkButton(frame_menu,text="Ver lista de Productos", fg_color="transparent", hover=False, text_color="#76ABAE",command=verProduct)
		boton2.configure(border_width=0, cursor="hand2")
		boton2.place(relx=0.08,rely=0.38,relwidth=0.80,relheight=0.10)


		def leave():
			resultado = messagebox.askquestion("Salir", '¿Estás seguro que quieres cerrar sesión?', icon='question', default='no')
			if resultado == 'yes':
				self.ventana.destroy()
				main.PantallaCarga()

		cerrar_sesion = ct.CTkButton(frame_left,text="Leave", fg_color="transparent", hover=False, text_color="#76ABAE",command=leave)
		cerrar_sesion.configure(border_width=0, cursor="hand2")
		cerrar_sesion.place(relx=0.08,rely=0.60,relwidth=0.80,relheight=0.10)



		self.ventana.iconphoto(True,icon_1)
		self.ventana.mainloop()
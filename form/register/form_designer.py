#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk
import util.generic as util
import os
from dotenv import load_dotenv
from tkinter import messagebox
import customtkinter as ct
from PIL import Image

load_dotenv()
icon = os.getenv('ICON')
Logo = os.getenv('LOGO')

class FormRegisterDesigner:

	def __init__(self):
		self.ventana = tk.Toplevel()
		self.ventana.title('Registrar Usuario')
		self.ventana.config(bg='#222831')
		self.ventana.resizable(width=0,height=0)
		util.centrar_ventana(self.ventana,700,500)

		my_image = ct.CTkImage(light_image=Image.open("./resources/Icono_Rework.png"),
			dark_image=Image.open("./resources/Icono_Rework.png"),
			size=(340,180))



		frame_form_top = tk.Frame(self.ventana,height=50,bd=0,relief=tk.SOLID,bg='#222831')
		frame_form_top.pack(side='top',fill=tk.BOTH,expand=tk.YES)

		title = ct.CTkLabel(frame_form_top,text='Registrar',font=('Dyuthi',30),fg_color='transparent',pady=17,text_color='#EEEEEE',bg_color='transparent')
		title.pack(padx=10,pady=1)
	
		frame1 = ct.CTkFrame(frame_form_top,width=360, height=350,fg_color='#31363F')
		frame1.place(relx=0.24,rely=0.11)

		logo = ct.CTkLabel(frame1,text='',image=my_image,fg_color='#31363F')
		logo.place(relx=0.02,rely=0.03)

		self.usuario = ct.CTkEntry(frame1,font=('Dyuthi',13),placeholder_text='Usuario',width=100,height=100)
		self.usuario.place(relx=0.24,rely=0.34,relwidth=0.55,relheight=0.10)

		self.password = ct.CTkEntry(frame1,font=('Dyuthi',13),placeholder_text='Contraseña',show='*',width=100,height=100)
		self.password.place(relx=0.24,rely=0.48,relwidth=0.55,relheight=0.10)

		self.confirmation = ct.CTkEntry(frame1,font=('Dyuthi',13),placeholder_text='Repetir Contraseña',show='*',width=100,height=100)
		self.confirmation.place(relx=0.24,rely=0.63,relwidth=0.55,relheight=0.10)

		register = ct.CTkButton(frame1,text='Registrar',font=('Dyuthi',18),fg_color='#222831',text_color='#EEEEEE',command=self.register)
		register.place(relx=0.22,rely=0.78,relwidth=0.57,relheight=0.15)
		register.bind('<Return>',(lambda event:self.register()))

		boton_salir = ct.CTkButton(frame_form_top,text='Salir',font=('Dyuthi',16),fg_color='#76ABAE',text_color='#222831',command=self.leave)
		boton_salir.place(relx=0.24,rely=0.83,relwidth=0.52,relheight=0.10)
		boton_salir.bind('<Return>',(lambda event:self.leave()))


		self.ventana.mainloop()

def register():
	pass
def leave():
	pass
#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk
import util.generic as util
from tkinter import messagebox
import os
from dotenv import load_dotenv
import customtkinter as ct
from PIL import Image

load_dotenv()
icon = os.getenv('ICON')
Logo = os.getenv('LOGO')

class FormLoginDesigner:
	def __init__(self):
		self.ventana = tk.Tk()
		self.ventana.title('Inicio de Sesion')
		self.ventana.geometry('800x500')
		self.ventana.config(bg='#222831')
		self.ventana.resizable(width=0,height=0)
		util.centrar_ventana(self.ventana,800,500)
		icon_1 = tk.PhotoImage(file='./resources/icons.ico')

		my_image = ct.CTkImage(light_image=Image.open("./resources/Icono_Rework-transformed.png"),
                                  dark_image=Image.open("./resources/Icono_Rework-transformed.png"),
                                  size=(600,250))

		frame_form_top = tk.Frame(self.ventana,height=50,bd=0,relief=tk.SOLID,bg='#222831')
		frame_form_top.pack(side='top',fill=tk.BOTH,expand=tk.YES)
		
		title = ct.CTkLabel(frame_form_top,text='Inicio de Sesión',font=('Dyuthi',30),fg_color='transparent',text_color='#EEEEEE',pady=50)
		title.pack(padx=10,pady=1)

		label = ct.CTkLabel(frame_form_top,text='',image=my_image,bg_color='#222831')
		label.pack(padx=1,pady=1)

		self.usuario = ct.CTkEntry(frame_form_top, placeholder_text="Usuario",font=('Dyuthi',14),width=300,height=30)
		self.usuario.place(x=250,y=280)

		self.password = ct.CTkEntry(frame_form_top, placeholder_text="Contraseña",font=('Dyuthi',14),width=300,height=30,show='*')
		self.password.place(x=250,y=340)

		inicio = ct.CTkButton(frame_form_top,text='Iniciar Sesión',font=('Dyuthi',15),fg_color='#31363F',text_color='#EEEEEE',bg_color='transparent',command=self.verificar)
		inicio.place(relx=0.095,rely=0.78,relwidth=0.40,relheight=0.10)
		inicio.bind('<Return>',(lambda event:self.verificar()))
		

		inicio = ct.CTkButton(frame_form_top,text='Registrar Usuario',font=('Dyuthi',15),fg_color='#31363F',text_color='#EEEEEE',bg_color='transparent',command=self.userRegister)
		inicio.place(relx=0.51,rely=0.78,relwidth=0.40,relheight=0.10)
		inicio.bind('<Return>',(lambda event:self.userRegister()))

		inicio = ct.CTkButton(frame_form_top,text='Salir',font=('Dyuthi',15),fg_color='#BF3131',text_color='#EEEEEE',bg_color='transparent',width=300,height=30,command=self.leave)
		inicio.place(x=200,y=450,relwidth=0.50,relheight=0.07)
		inicio.bind('<Return>',(lambda event:self.leave()))

		
		self.ventana.iconphoto(True,icon_1)
		self.ventana.mainloop()

def verificar():
	pass
def userRegister():
	pass
def leave():
	pass
#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk
import util.generic as util
from tkinter import messagebox
import os
from dotenv import load_dotenv
import customtkinter as ct 

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

		frame_form = tk.Frame(self.ventana,bd=0,relief=tk.SOLID,bg='#222831')
		frame_form.pack(side='right',expand=tk.YES,fill=tk.BOTH)

		frame_form_top = tk.Frame(frame_form,height=50,bd=0,relief=tk.SOLID,bg='#222831')
		frame_form_top.pack(side='top',fill=tk.X)
		
		title = ct.CTkLabel(frame_form_top,text='Inicio de Sesión',font=('Dyuthi',30),fg_color='transparent',text_color='#EEEEEE',pady=50)
		title.pack(expand=tk.YES,fill=tk.BOTH)

		frame_form_fill = tk.Frame(frame_form,height=50,bd=0,relief=tk.SOLID,bg='#222831')
		frame_form_fill.pack(side='bottom',expand=tk.YES,fill=tk.BOTH)

		self.usuario = ct.CTkEntry(frame_form_fill, placeholder_text="Usuario",font=('Dyuthi',14),width=300,height=30)
		self.usuario.pack(padx=20,pady=5)

		self.password = ct.CTkEntry(frame_form_fill, placeholder_text="Contraseña",font=('Dyuthi',14),width=300,height=30,show='*')
		self.password.pack(padx=20,pady=40)

		inicio = ct.CTkButton(frame_form_fill,text='Iniciar Sesión',font=('Dyuthi',15),fg_color='#31363F',text_color='#EEEEEE',bg_color='transparent',command=self.verificar)
		inicio.pack(padx=20,pady=5)
		inicio.bind('<Return>',(lambda event:self.verificar()))
		

		inicio = ct.CTkButton(frame_form_fill,text='Registrar Usuario',font=('Dyuthi',15),fg_color='#31363F',text_color='#EEEEEE',bg_color='transparent',command=self.userRegister)
		inicio.pack(padx=20,pady=5)
		inicio.bind('<Return>',(lambda event:self.userRegister()))

		inicio = ct.CTkButton(frame_form_fill,text='Salir',font=('Dyuthi',15),fg_color='#31363F',text_color='#EEEEEE',bg_color='transparent',command=self.leave)
		inicio.pack(padx=20,pady=5)
		inicio.bind('<Return>',(lambda event:self.leave()))

		
		self.ventana.iconphoto(True,icon_1)
		self.ventana.mainloop()

def verificar():
	pass
def userRegister():
	pass
def leave():
	pass
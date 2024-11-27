#!/usr/bin/env python3

from form.login.form_login import FormLogin
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import util.generic as util
import os
from dotenv import load_dotenv
import time
import customtkinter as ct
from PIL import Image


class PantallaCarga:
	def __init__(self):
		self.ventana = tk.Tk()
		self.ventana.title('Cargando Login')
		self.ventana.config(bg='#222831')
		self.ventana.resizable(width=0,height=0)
		util.centrar_ventana(self.ventana,600,300)
		my_image = ct.CTkImage(light_image=Image.open("./resources/Icono_Rework-transformed.png"),
                                  dark_image=Image.open("./resources/Icono_Rework-transformed.png"),
                                  size=(600,300))
		icon_1 = tk.PhotoImage(file='./resources/icons.ico')
		self.task = 100
		self.x = 0
		self.label = ct.CTkLabel(self.ventana,text='Cargando Login de InvenTech',font=('Dyuthi',16),fg_color='transparent',text_color='#EEEEEE')
		self.label.pack(padx=10,pady=5)
		self.label1 = ct.CTkLabel(self.ventana,image=my_image,text="")
		self.label1.pack(padx=0.1,pady=0.1)

		self.bar = ct.CTkProgressBar(self.ventana,orientation='horizontal',
			width=300,
			height=30,
			mode='determinate',
			corner_radius=20,
			border_width=2,
			fg_color='#31363F',
			border_color='#76ABAE',
			progress_color='#EEEEEE',
			determinate_speed=0.5,
			indeterminate_speed=0.5)
		self.bar.place(x=155,y=200)
		self.bar.set(0)
		
		while(self.x<self.task):
			time.sleep(0.1)
			self.bar.step()
			self.x+=1
			self.percent = ct.CTkLabel(self.ventana,text=f'{int((self.x/self.task)*100)}%',font=('Dyuthi',13),fg_color='transparent',text_color='#EEEEEE')
			self.percent.place(x=478,y=200)
			self.ventana.update_idletasks()
		if self.x == self.task:
			time.sleep(0.5)
			self.ventana.destroy()
			FormLogin()

		self.ventana.mainloop()


if __name__ == '__main__':
	PantallaCarga()

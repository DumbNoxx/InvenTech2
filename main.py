#!/usr/bin/env python3
from form.login.form_login import FormLogin
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import util.generic as util
import os
from dotenv import load_dotenv
import time


class PantallaCarga:
	def __init__(self):
		self.ventana = tk.Tk()
		self.ventana.title('Cargando Login')
		self.ventana.resizable(width=0,height=0)
		util.centrar_ventana(self.ventana,600,300)
		logo = util.leer_image('./resources/logotipo.png',(200,200))
		icon_1 = tk.PhotoImage(file='./resources/icons.ico')
		self.task = 100
		self.x = 0
		self.label = tk.Label(self.ventana,text='Cargando Login de InvenTech',font=('Dyuthi',14))
		self.label.pack(padx=10,pady=10)
		self.label1 = tk.Label(self.ventana,image=logo)
		self.label1.pack(padx=10,pady=10)
		self.bar = Progressbar(self.ventana,orient=tk.HORIZONTAL,length=350)
		self.bar.pack(padx=10,pady=10)
		self.ventana.iconphoto(True,icon_1)
		while(self.x<self.task):
			time.sleep(0.3)
			self.bar['value']+=1
			self.x+=1
			self.percent = tk.Label(self.ventana,text=f'{int((self.x/self.task)*100)}%',font=('Dyuthi',11))
			self.percent.place(x=478,y=270)
			self.ventana.update_idletasks()
		if self.x == self.task:
			time.sleep(0.5)
			self.ventana.destroy()
			FormLogin()
		
		self.ventana.mainloop()


if __name__ == '__main__':
	PantallaCarga()

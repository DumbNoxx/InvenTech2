#!/usr/bin/env python3
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import util.generic as util
import time
from tkinter import messagebox
from persistence.repository.auth_user_repository import AuthUserRepository
from persistence.model import Inventary

class BarraProgresiva:
	def __init__(self):
		self.auth_repository = AuthUserRepository()
		self.ventana = tk.Toplevel()
		self.ventana.title('Cargando')
		self.ventana.resizable(width=0,height=0)
		util.centrar_ventana(self.ventana,400,100)
		self.lens = len(self.auth_repository.getProductInInventary())
		self.task = self.lens
		self.x = 0
		self.label = tk.Label(self.ventana,text='Cargando Inventario')
		self.label.pack(padx=10,pady=10)
		self.bar = Progressbar(self.ventana,orient=tk.HORIZONTAL,length=350)
		self.bar.pack(padx=10,pady=10)
		print(self.task)
		while(self.x<self.task):
			time.sleep(1)
			self.bar['value']+=0
			if self.task <= 1:
				self.bar['value']+=100
			elif self.task <= 2:
				self.bar['value']+=50
			elif self.task <= 3:
				self.bar['value']+=33.33
			elif self.task <= 4:
				self.bar['value']+=25
			elif self.task <= 5:
				self.bar['value']+=20
			elif self.task <= 6:
				self.bar['value']+=16.66
			elif self.task <= 7:
				self.bar['value']+=14.28
			elif self.task <= 8:
				self.bar['value']+=12.5
			elif self.task <= 9:
				self.bar['value']+=11.11
			elif self.task <= 10:
				self.bar['value']+=10

			self.x+=1
			if self.task >= 11:
				if self.bar['value'] == 0:
					self.bar['value']+=(self.x/(self.task))*100
				else:
					self.bar['value']=(self.x/(self.task))*100

			
			self.percent = tk.Label(self.ventana,text=f'{int((self.x/self.task)*100)}%')
			self.percent.place(x=180,y=80)
			self.ventana.update_idletasks()
		if self.x == self.task:
			time.sleep(0.5)
			self.ventana.destroy()
			messagebox.showinfo(message='Inventario Cargado satisfactoria mente',title='Listo')



if __name__ == '__main__':
	BarraProgresiva()

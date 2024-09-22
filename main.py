from form.login.form_login import FormLogin
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import util.generic as util
import time

class PantallaCarga:
	def __init__(self):
		self.ventana = tk.Tk()
		self.ventana.title('Cargando Login')
		self.ventana.resizable(width=0,height=0)
		util.centrar_ventana(self.ventana,600,300)
		logo = util.leer_image('./resources/designer/logo.png',(200,200))
		self.task = 20
		self.x = 0
		self.label = tk.Label(self.ventana,text='Cargando Login de InvenTech')
		self.label.pack(padx=10,pady=10)
		self.label1 = tk.Label(self.ventana,image=logo)
		self.label1.pack(padx=10,pady=10)
		self.bar = Progressbar(self.ventana,orient=tk.HORIZONTAL,length=350)
		self.bar.pack(padx=10,pady=10)
		while(self.x<self.task):
			time.sleep(1)
			self.bar['value']+=5
			self.x+=1
			self.ventana.update_idletasks()
		if self.x == self.task:
			time.sleep(0.5)
			self.ventana.destroy()
			FormLogin()
		self.ventana.mainloop()


if __name__ == '__main__':
	PantallaCarga()

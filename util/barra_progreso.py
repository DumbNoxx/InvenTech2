from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import util.generic as util
import time

class BarraProgresiva:
	def __init__(self):
		self.ventana = tk.Toplevel()
		self.ventana.title('Cargando')
		self.ventana.resizable(width=0,height=0)
		util.centrar_ventana(self.ventana,400,100)
		self.task = 20
		self.x = 0
		self.label = tk.Label(self.ventana,text='Cargando Inventario')
		self.label.pack(padx=10,pady=10)
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


if __name__ == '__main__':
	BarraProgresiva()

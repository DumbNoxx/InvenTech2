from tkinter import *
import tkinter as tk
import util.generic as util

class FacturarProductDesginer:

	def __init__(self):
		self.ventana = tk.Toplevel()
		self.ventana.title('Facturar Producto')
		self.ventana.resizable(width=0,height=0)
		self.ventana.config(bg='#fcfcfc')
		util.centrar_ventana(self.ventana,600,400)

		frame_top = tk.Frame(self.ventana,bg='red',bd=0,width=200,relief=tk.SOLID,padx=5,pady=5)
		frame_top.pack(side='top',expand=tk.YES,fill=tk.BOTH)

		

		frame_fill = tk.Frame(self.ventana,bd=0,width=200,relief=tk.SOLID,padx=5,pady=5,bg='yellow')
		frame_fill.pack(side='bottom',expand=tk.YES,fill=tk.BOTH)



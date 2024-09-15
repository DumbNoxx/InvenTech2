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


#!/usr/bin/env python3
from tkinter import *
import tkinter as tk
from tkinter import ttk
import util.generic as util

class FacturarProductDesginer:

	def __init__(self):
		self.ventana = tk.Toplevel()
		self.ventana.title('Facturar Producto')
		self.ventana.resizable(width=0,height=0)
		self.ventana.config(bg='#6BABF5')
		util.centrar_ventana(self.ventana,700,450)
		logo = util.leer_image('./resources/logotipo.png',(180,180))

		frame_top = tk.Frame(self.ventana,bg='#6BABF5',bd=0,width=200,relief=tk.SOLID,padx=5,pady=5)
		frame_top.pack(side='top',expand=tk.YES,fill=tk.BOTH)

		self.title = tk.Label(frame_top,text='Facturar Producto',font=('Dyuthi',24),fg='black',bg='#6BABF5')
		self.title.pack(expand=tk.NO,fill=tk.BOTH)

		frame_fill = tk.Frame(self.ventana,bd=0,width=200,relief=tk.SOLID,padx=5,pady=5,bg='#6BABF5')
		frame_fill.pack(side='bottom',expand=tk.YES,fill=tk.BOTH)

		frame_logo = tk.Frame(frame_fill,bg='#6BABF5',bd=0,width=180,height=180,relief=tk.SOLID,padx=3,pady=3)
		frame_logo.pack()

		logos = tk.Label(frame_logo,image=logo,bg='#6BABF5')
		logos.pack()

		self.subtitle = tk.Label(frame_fill,text='Serial del Producto',font=('Dyuthi',16),fg='black',bg='#6BABF5')
		self.subtitle.pack(fill=tk.Y,padx=4,pady=4)

		self.entrada = ttk.Entry(frame_fill,font=('Dyuthi',14))
		self.entrada.pack(fill=tk.Y,padx=4,pady=4)

		self.subtitle2 = tk.Label(frame_fill,text='Cantidad',font=('Dyuthi',14),fg='black',bg='#6BABF5')
		self.subtitle2.pack(fill=tk.Y,padx=4,pady=4)

		self.entrada2 = ttk.Entry(frame_fill,font=('Dyuthi',16))
		self.entrada2.pack(fill=tk.Y,padx=4,pady=4)

		self.boton_facturar = tk.Button(frame_fill,text='Facturar',bg='#6BABF5',fg='black',font=('Dyuthi',14))
		self.boton_facturar.pack(fill=tk.Y,padx=4,pady=4)

		self.leave = tk.Button(frame_fill,text='Salir',bg='#6BABF5',fg='black',font=('Dyuthi',14),command=self.leave)
		self.leave.pack(fill=tk.Y,padx=4,pady=4)
		self.leave.bind('<Return>',(lambda event:self.leave()))

		self.ventana.mainloop()


def leave():
	pass

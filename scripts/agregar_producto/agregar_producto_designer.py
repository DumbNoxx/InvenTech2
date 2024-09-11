import tkinter as tk
from tkinter import *
from tkinter import ttk
from persistence.model import Inventary
from persistence.repository.inventary_repository import InventaryRepository
import util.generic as util
from tkinter import messagebox


class AgregarProductoDesigner:

	def __init__(self):
		self.ventana = tk.Toplevel()
		self.ventana.title('Agregar Producto')
		util.centrar_ventana(self.ventana,600,350)
		self.ventana.config(bg='#fad7a0')

		logo = util.leer_image('./resources/logo.png',(200,200))

		frame_logo = tk.Frame(self.ventana,bd=0,width=200,relief=tk.SOLID,padx=5,pady=5,bg='#f7dc6f')
		frame_logo.pack(side='left',expand=False,fill=tk.BOTH)
		label = tk.Label(frame_logo,image=logo,bg='#f7dc6f')
		label.place(x=0,y=0,relwidth=1,relheight=1)

		frame_top = tk.Frame(self.ventana,height=20,bd=0,relief=tk.SOLID,bg='#fad7a0')
		frame_top.pack(side='top',expand=tk.YES,fill=tk.BOTH)

		titulo_ventana = tk.Label(frame_top,text='Agregar Producto',font=('Dyuthi',24),fg='black',bg='#fad7a0')
		titulo_ventana.pack(expand=tk.YES,fill=tk.BOTH)

		frame_fill = tk.Frame(self.ventana,height=50,bd=0,relief=tk.SOLID,bg='#fad7a0')
		frame_fill.pack(side='bottom',expand=tk.YES,fill=tk.BOTH)

		nombre_producto = tk.Label(frame_fill,text='Ingresa el nombre del producto',font=('Dyuthi',12),fg='black',bg='#fad7a0')
		nombre_producto.pack(fill=tk.X,padx=20,pady=10)

		nombre_producto = ttk.Entry(frame_fill,font=('Dyuthi',11))
		nombre_producto.pack(fill=tk.Y,padx=5,pady=5)

		serial_producto = tk.Label(frame_fill,text='Ingresa el serial del producto',font=('Dyuthi',12),fg='black',bg='#fad7a0')
		serial_producto.pack(fill=tk.X,padx=20,pady=10)

		serial_producto = ttk.Entry(frame_fill,font=('Dyuthi',11))
		serial_producto.pack(fill=tk.Y,padx=5,pady=5)

		cantidad_producto = tk.Label(frame_fill,text='Ingresa la cantidad de productos que recibiste',font=('Dyuthi',12),fg='black',bg='#fad7a0')
		cantidad_producto.pack(fill=tk.X,padx=20,pady=10)

		cantidad_producto = ttk.Entry(frame_fill,font=('Dyuthi',11))
		cantidad_producto.pack(fill=tk.Y,padx=5,pady=5)

		boton_agregar = tk.Button(frame_fill,text='Agregar Producto',font=('Dyuthi',12),bg='#f7dc6f',fg='black')
		boton_agregar.pack(fill=tk.X,padx=20,pady=10)

		def leave():
			resultado = messagebox.askquestion("Salir", '¿Estás seguro qué deseas salir?', icon='question', default='no')
			if resultado == 'yes':
				self.ventana.destroy()

		boton_salir = tk.Button(frame_fill,text='Salir',font=('Dyuthi',12),bg='#f7dc6f',fg='black',command=leave)
		boton_salir.pack(fill=tk.X,padx=10,pady=10)

		self.ventana.mainloop()
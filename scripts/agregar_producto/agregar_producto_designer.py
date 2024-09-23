#!/usr/bin/env python3
import tkinter as tk
from tkinter import *
from tkinter import ttk
import util.generic as util
from tkinter import messagebox


class AgregarProductoDesigner:

	def __init__(self):
		self.ventana = tk.Toplevel()
		self.ventana.title('Agregar Producto')
		util.centrar_ventana(self.ventana,700,450)
		self.ventana.config(bg='#fad7a0')
		self.ventana.resizable(width=0,height=0)

		logo = util.leer_image('./resources/designer/logo.png',(200,200))

		frame_logo = tk.Frame(self.ventana,bd=0,width=200,relief=tk.SOLID,padx=5,pady=5,bg='#f7dc6f')
		frame_logo.pack(side='left',expand=False,fill=tk.BOTH)

		
		label = tk.Label(frame_logo,image=logo,bg='#f7dc6f')
		label.place(x=0,y=0,relwidth=1,relheight=1)

		copyrigth = tk.Label(frame_logo,text='Nox Corporations ©',width=30,padx=3,pady=3,bg='#f7dc6f',font=('Dyuthi',10))
		copyrigth.grid(column=0,row=0)

		frame_top = tk.Frame(self.ventana,height=20,bd=0,relief=tk.SOLID,bg='#fad7a0')
		frame_top.pack(side='top',expand=tk.YES,fill=tk.BOTH)

		titulo_ventana = tk.Label(frame_top,text='Agregar Producto',font=('Dyuthi',24),fg='black',bg='#fad7a0')
		titulo_ventana.pack(expand=tk.YES,fill=tk.BOTH)

		frame_fill = tk.Frame(self.ventana,height=50,bd=0,relief=tk.SOLID,bg='#fad7a0')
		frame_fill.pack(side='bottom',expand=tk.YES,fill=tk.BOTH)

		etiqueta_nombre_producto = tk.Label(frame_fill,text='Ingresa el nombre del producto',font=('Dyuthi',12),fg='black',bg='#fad7a0')
		etiqueta_nombre_producto.pack(fill=tk.X,padx=20,pady=10)

		self.nombre_producto = ttk.Entry(frame_fill,font=('Dyuthi',11))
		self.nombre_producto.pack(fill=tk.Y,padx=5,pady=5)

		etiqueta_serial_producto = tk.Label(frame_fill,text='Ingresa el serial del producto',font=('Dyuthi',12),fg='black',bg='#fad7a0')
		etiqueta_serial_producto.pack(fill=tk.X,padx=20,pady=10)

		self.serial_producto = ttk.Entry(frame_fill,font=('Dyuthi',11))
		self.serial_producto.pack(fill=tk.Y,padx=5,pady=5)

		etiqueta_cantidad_producto = tk.Label(frame_fill,text='Ingresa la cantidad de productos que recibiste',font=('Dyuthi',12),fg='black',bg='#fad7a0')
		etiqueta_cantidad_producto.pack(fill=tk.X,padx=20,pady=10)

		self.cantidad_producto = ttk.Entry(frame_fill,font=('Dyuthi',11))
		self.cantidad_producto.pack(fill=tk.Y,padx=5,pady=5)

		etiqueta_precio_producto = tk.Label(frame_fill,text='Ingresa el precio del producto',font=('Dyuthi',12),fg='black',bg='#fad7a0')
		etiqueta_precio_producto.pack(fill=tk.X,padx=20,pady=10)

		self.precio_producto = ttk.Entry(frame_fill,font=('Dyuthi',11))
		self.precio_producto.pack(fill=tk.Y,padx=5,pady=5)

		boton_agregar = tk.Button(frame_fill,text='Agregar Producto',font=('Dyuthi',12),bg='#f7dc6f',fg='black',command=self.Add)
		boton_agregar.pack(fill=tk.X,padx=20,pady=10)
		boton_agregar.bind('<Return>',(lambda event:self.Add()))

		boton_salir = tk.Button(frame_fill,text='Salir',font=('Dyuthi',12),bg='#f7dc6f',fg='black',command=self.leave)
		boton_salir.pack(fill=tk.X,padx=10,pady=10)
		boton_salir.bind('<Return>',(lambda event:self.leave()))

		self.ventana.mainloop()



def Add():
	pass
def leave():
	pass
#!/usr/bin/env python3
from tkinter import *
import tkinter as tk
import util.generic as util

class FacturarProductDesginer:

	def __init__(self):
		self.ventana = tk.Toplevel()
		'''self.ventana.title('Facturar Producto')'''
		self.ventana.title('[En proceso]')
		self.ventana.resizable(width=0,height=0)
		'''self.ventana.config(bg='#6BABF5')'''
		self.ventana.config(bg='#fcfcfc')
		util.centrar_ventana(self.ventana,697,433)

		'''frame_top = tk.Frame(self.ventana,bg='#6BABF5',bd=0,width=200,relief=tk.SOLID,padx=5,pady=5)
								frame_top.pack(side='top',expand=tk.YES,fill=tk.BOTH)
								
								
								frame_fill = tk.Frame(self.ventana,bd=0,width=200,relief=tk.SOLID,padx=5,pady=5,bg='#6BABF5')
								frame_fill.pack(side='bottom',expand=tk.YES,fill=tk.BOTH)
						'''
		logo = util.leer_image('./resources/notfounds.png',(150,150))

		frame_logo = tk.Frame(self.ventana,bd=0,width=200,height=200,relief=tk.SOLID,padx=5,pady=5,bg='#fcfcfc')
		frame_logo.pack(side='top',expand=True,fill=tk.BOTH)

		text = tk.Label(self.ventana,text="Ventana en proceso, por favor salir.",bg='#fcfcfc',fg='black',font=('Dyuthi',18))
		text.pack()

		label = tk.Label(frame_logo,image=logo,bg='#fcfcfc')
		label.place(x=0,y=0,relwidth=1,relheight=1)

		flecha = util.leer_image('./resources/designers/flechas.png',(100,100))
		frame_fill = tk.Frame(self.ventana,bd=0,width=200,height=200,relief=tk.SOLID,padx=5,pady=5,bg='#fcfcfc')
		frame_fill.pack(side='bottom',expand=True,fill=tk.BOTH)
		label1 = tk.Label(frame_fill,image=flecha,bg='#fcfcfc')
		label1.pack()
		boton_salir = tk.Button(frame_fill,text='Salir',bg='red',command=self.leave)
		boton_salir.pack()
		boton_salir.bind('<Return>',(lambda event:self.leave()))


		self.ventana.mainloop()


def leave():
	pass
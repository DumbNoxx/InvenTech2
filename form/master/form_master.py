import tkinter as tk
from tkinter.font import BOLD
import util.generic as util
import os
from dotenv import load_dotenv
from scripts.calculadora.calculadora import CalculadoraCreate
import subprocess
from tkinter import messagebox


load_dotenv()
Logo = os.getenv('LOGO')
Login = os.getenv('LOGIN')


class MasterPanel:
	def __init__(self):
		self.ventana = tk.Tk()
		self.ventana.title('InvenTech')
		w,h = self.ventana.winfo_screenwidth(),self.ventana.winfo_screenheight()
		self.ventana.geometry("%dx%d+0+0" % (w,h))
		self.ventana.config(bg='#09ab53')
		self.ventana.resizable(width=0,height=0)

		logo = util.leer_image(Logo,(350,350))

		label1 = tk.Label(self.ventana,image=logo,bg='#1abc9c')
		label1.place(x=0,y=0,relwidth=1,relheight=1)

		label_title = tk.Label(self.ventana,text='InvenTech',bg='#1abc9c',font=('Dyuthi',36),fg='#f4d03f')
		label_title.place(x=70,y=40,relwidth=0.9,relheight=0.05)
		label_description = tk.Label(self.ventana,text='Sistema de Inventario',bg='#1abc9c',font=('Dyuthi',18),fg='#f4d03f')
		label_description.place(x=70,y=90,relwidth=0.9,relheight=0.03)

		def calcu():
			CalculadoraCreate().mainloop()

		boton = tk.Button(self.ventana,text='Calculadora',bg='#a3e4d7',font=('Dyuthi',12),fg='black',command=calcu)
		boton.place(x=620,y=170,relwidth=0.09,relheight=0.07)

		boton1 = tk.Button(self.ventana,text='Agregar Producto',bg='#a3e4d7',font=('Dyuthi',12),fg='black')
		boton1.place(x=450,y=200,relwidth=0.09,relheight=0.07)

		def leave():
			resultado = messagebox.askquestion("Salir", '¿Estás seguro que quieres cerrar sesión?', icon='question', default='no')
			if resultado == 'yes':
				self.ventana.destroy()
				subprocess.run(['python3',Login])

		cerrar_sesion = tk.Button(self.ventana,text='Cerrar Sesion',bg='#a3e4d7',font=('Dyuthi',12),fg='black',command=leave)
		cerrar_sesion.place(x=10,y=600,relwidth=0.09,relheight=0.07)

		self.ventana.mainloop()
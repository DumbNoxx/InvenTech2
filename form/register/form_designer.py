import tkinter as tk
from tkinter import ttk
import util.generic as util
import os
from dotenv import load_dotenv
from tkinter import messagebox

load_dotenv()
icon = os.getenv('ICON')


class FormRegisterDesigner:

	def __init__(self):
		self.ventana = tk.Toplevel()
		self.ventana.title('Registrar Usuario')
		self.ventana.config(bg='#fcfcfc')
		self.ventana.resizable(width=0,height=0)
		util.centrar_ventana(self.ventana,700,500)

		

		logo = util.leer_image('./resources/designer/logo.png',(200,200))

		frame_logo = tk.Frame(self.ventana,bd=0,width=300,relief=tk.SOLID,padx=10,pady=10,bg='#78c2e2')
		frame_logo.pack(side='left',expand=tk.NO,fill=tk.BOTH)
		label = tk.Label(frame_logo,image=logo,bg='#78c2e2')
		label.place(x=0,y=0,relwidth=1,relheight=1)

		frame_form = tk.Frame(self.ventana,bd=0,relief=tk.SOLID,bg='#afaeb0')
		frame_form.pack(side='right',expand=tk.YES,fill=tk.BOTH)

		frame_form_top = tk.Frame(frame_form,height=50,bd=0,relief=tk.SOLID,bg='black')
		frame_form_top.pack(side='top',fill=tk.X)
		title = tk.Label(frame_form_top,text='Registrar',font=('Dyuthi',30),fg='black',bg='#afaeb0',pady=50)
		title.pack(expand=tk.YES,fill=tk.BOTH)

		frame_form_fill = tk.Frame(frame_form,height=50,bd=0,relief=tk.SOLID,bg='#afaeb0')
		frame_form_fill.pack(side='bottom',expand=tk.YES,fill=tk.BOTH)

		etiqueta_usuario = tk.Label(frame_form_fill,text='Usuario',font=('Dyuthi',14),fg='black',bg='#afaeb0',anchor='w')
		etiqueta_usuario.pack(fill=tk.X,padx=20,pady=5)
		self.usuario = ttk.Entry(frame_form_fill,font=('Dyuthi',14))
		self.usuario.pack(fill=tk.X,padx=20,pady=10)
		etiqueta_password = tk.Label(frame_form_fill,text='Contraseña',font=('Dyuthi',14),fg='black',bg='#afaeb0',anchor='w')
		etiqueta_password.pack(fill=tk.X,padx=20,pady=5)
		self.password = ttk.Entry(frame_form_fill,font=('Dyuthi',14))
		self.password.pack(fill=tk.X,padx=20,pady=10)
		self.password.config(show='*')

		etiqueta_confirmation = tk.Label(frame_form_fill,text='Repetir Contraseña',font=('Dyuthi',14),fg='black',bg='#afaeb0',anchor='w')
		etiqueta_confirmation.pack(fill=tk.X,padx=20,pady=5)
		self.confirmation = ttk.Entry(frame_form_fill,font=('Dyuthi',14))
		self.confirmation.pack(fill=tk.X,padx=20,pady=10)
		self.confirmation.config(show='*')
		

		register = tk.Button(frame_form_fill,text='Registrar',font=('Dyuthi',15),bg='#8f68b5',bd=0,fg='black',command=self.register)
		register.pack(fill=tk.X,padx=10,pady=10)
		register.bind('<Return>',(lambda event:self.register()))
		
		def leave():
			resultado = messagebox.askquestion("Salir", '¿Estás seguro que quieres salir de la ventana?', icon='question', default='no')
			if resultado == 'yes':
				self.ventana.destroy()
		boton_salir = tk.Button(frame_form_fill,text='Salir',font=('Dyuthi',11),bg='#8f68b5',bd=0,fg='black',command=leave)
		boton_salir.pack(fill=tk.X,padx=10,pady=10)

		self.ventana.mainloop()

def register():
	pass
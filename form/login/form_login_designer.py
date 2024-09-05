import tkinter as tk
from tkinter import ttk
import util.generic as util

class FormLoginDesigner:

	def verificar(self):
		pass
	def userRegister(self):
		pass

	def __init__(self):
		self.ventana = tk.Tk()
		self.ventana.title('Inicio de Sesion')
		self.ventana.geometry('800x500')
		self.ventana.config(bg='#fcfcfc')
		self.ventana.resizable(width=0,height=0)
		util.centrar_ventana(self.ventana,800,500)

		

		logo = util.leer_image('./resources/logo.png',(200,200))

		frame_logo = tk.Frame(self.ventana,bd=0,width=300,relief=tk.SOLID,padx=10,pady=10,bg='#abb2b9')
		frame_logo.pack(side='left',expand=tk.NO,fill=tk.BOTH)
		label = tk.Label(frame_logo,image=logo,bg='#abb2b9')
		label.place(x=0,y=0,relwidth=1,relheight=1)
		copyrigth = tk.Label(frame_logo,text='Nox Corporations ©',width=40,padx=6,pady=6,bg='#abb2b9',font=('Dyuthi',10))
		copyrigth.grid(column=0,row=0)


		frame_form = tk.Frame(self.ventana,bd=0,relief=tk.SOLID,bg='#ccd1d1')
		frame_form.pack(side='right',expand=tk.YES,fill=tk.BOTH)

		frame_form_top = tk.Frame(frame_form,height=50,bd=0,relief=tk.SOLID,bg='black')
		frame_form_top.pack(side='top',fill=tk.X)
		title = tk.Label(frame_form_top,text='Inicio de Sesión',font=('Dyuthi',30),fg='black',bg='#afaeb0',pady=50)
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

		inicio = tk.Button(frame_form_fill,text='Iniciar Sesión',font=('Dyuthi',15),bg='#8f68b5',bd=0,fg='black',command=self.verificar)
		inicio.pack(fill=tk.X,padx=20,pady=20)
		inicio.bind('<Return>',(lambda event:self.verificar()))
		
		inicio = tk.Button(frame_form_fill,text='Registrar Usuario',font=('Dyuthi',15),bg='#8f68b5',bd=0,fg='black',command=self.userRegister)
		inicio.pack(fill=tk.X,padx=20,pady=20)
		inicio.bind('<Return>',(lambda event:self.userRegister()))
		

		self.ventana.mainloop()

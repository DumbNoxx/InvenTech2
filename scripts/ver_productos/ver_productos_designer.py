from persistence.repository.auth_user_repository import AuthUserRepository
import tkinter as tk
from tkinter import ttk
import util.generic as util
from tkinter import messagebox
from persistence.model import Inventary
from sqlalchemy.orm import Session
import sqlalchemy as db

class VerProductosDesigner:

	def __init__(self):
		self.engine = db.create_engine('sqlite:///db/login.sqlite',echo=False,future=True)
		self.ventana = tk.Toplevel()
		self.ventana.title('Ver Productos')
		self.ventana.config(bg='#fcfcfc')
		self.ventana.resizable(width=0,height=0)
		util.centrar_ventana(self.ventana,800,400)

		logo = util.leer_image('./resources/designer/logo.png',(100,100))

		self.frame_top = tk.Frame(self.ventana,height=20,width=5,bd=0,relief=tk.SOLID,bg='#ec7063')
		self.frame_top.pack(side='top',expand=tk.YES,fill=tk.BOTH)

		titulo_ventana = tk.Label(self.frame_top,text='Ver Productos',bg='#ec7063',fg='black',font=('Dyuthi',30))
		titulo_ventana.pack(expand=tk.YES,fill=tk.BOTH)

		frame_copyright = tk.Frame(titulo_ventana,bd=0,width=200,height=200,bg='#ec7063')
		frame_copyright.place(x=90,y=10,relwidth=0.2,relheight=0.25)


		copyright = tk.Label(frame_copyright,text='Nox Corporations ©',font=('Dyuthi',8),bg='#ec7063',fg='black')
		copyright.pack()

		frame_logo = tk.Frame(titulo_ventana,bd=1,width=100,height=100,bg='#ec7063')
		frame_logo.grid(column=0,row=0)
		label = tk.Label(frame_logo,image=logo,bg='#ec7063')
		label.place(x=0,y=0,relwidth=1,relheight=1)

		frame_boton = tk.Frame(titulo_ventana,bd=1,width=50,height=50,bg='#ec7063')
		frame_boton.place(x=670,y=10,relwidth=0.2,relheight=0.25)

		def leave():
			resultado = messagebox.askquestion("Salir", '¿Estás seguro qué deseas salir de la ventana?', icon='question', default='no')
			if resultado == 'yes':
				self.ventana.destroy()

		boton_leave = tk.Button(frame_boton,text='Salir',font=('Dyuthi',11),bg='#a93226',fg='black',command=leave)
		boton_leave.pack()

		texto_principal = tk.Label(self.frame_top,text='Ingresa el nombre del producto a buscar',font=('Dyuthi',12),bg='#ec7063',fg='black',)
		texto_principal.pack(expand=tk.YES,fill=tk.BOTH)

		self.entrada_principal = ttk.Entry(self.frame_top,font=('Dyuthi',11))
		self.entrada_principal.pack(fill=tk.Y,padx=5,pady=5)
			
		boton_principal_buscar = tk.Button(self.frame_top,text='Buscar',bg='#a93226',fg='black',font=('Dyuthi',11),command=self.Buscar)
		boton_principal_buscar.pack(fill=tk.Y,padx=5,pady=5)
		boton_principal_buscar.bind('<Return>',(lambda event:self.Buscar()))

		self.frame_fill = tk.Frame(self.ventana,height=20,width=6,bd=0,relief=tk.SOLID,bg='gray')
		self.frame_fill.pack(side='bottom',expand=tk.YES,fill=tk.BOTH)

		self.tree = ttk.Treeview(self.frame_fill,height=10, columns=[f"#{n}" for n in range(1, 4)])
		self.tree.grid(row=0, column=0)
		self.tree.heading('#0', text='ID',anchor=tk.CENTER)
		self.tree.heading('#1', text='Producto',anchor=tk.CENTER)
		self.tree.heading('#2', text='Inventario',anchor=tk.CENTER)
		self.tree.heading('#3', text='Precio',anchor=tk.CENTER)
		self.auth_repository = AuthUserRepository()
		prod:Inventary = self.auth_repository.getProductInInventary()
		
		for prods in prod:
			self.tree.insert('',tk.END,text=prods.id,value=(prods.name_product,f'{prods.inventary_product} unidades',f'{prods.price_product}$'))

		self.ventana.mainloop()


def Buscar():
	pass
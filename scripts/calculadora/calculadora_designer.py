import tkinter as tk
from tkinter import *
from tkinter import ttk
import math

class CalculadoraDesigner:

	

	def __init__(self):
		def ingresarValores(tecla):
			if tecla >= '0' and tecla <= '9' or tecla == '(' or tecla == ')' or tecla == '.':
				entrada2.set(entrada2.get() + tecla)

			if tecla == '*' or tecla == '/' or tecla == '+' or tecla == '-':
				if tecla == '*':
					entrada1.set(entrada2.get() + '*')
				elif tecla == '/':
					entrada1.set(entrada2.get() + '/')
				elif tecla == '+':
					entrada1.set(entrada2.get() + '+')
				elif tecla == "-":
					entrada1.set(entrada2.get() + '-')

				entrada2.set('')

			if tecla == '=':
				entrada1.set(entrada1.get() + entrada2.get())
				resultado = eval(entrada1.get())
				entrada2.set(resultado)

		def raizcuadradra():
			entrada1.set('')
			resultado = math.sqrt(float(entrada2.get()))
			entrada2.set(resultado)

		def borrar(*event):
			inicio = 0
			final = len(entrada2.get())

			entrada2.set(entrada2.get()[inicio:final-1])

		def borrar_todo(*event):
			entrada1.set('')
			entrada2.set('')

		def ingresarValoresTeclado(event):
			tecla = event.char

			if tecla >= '0' and tecla <= '9' or tecla == '(' or tecla == ')' or tecla == '.':
				entrada2.set(entrada2.get() + tecla)

			if tecla == '*' or tecla == '/' or tecla == '+' or tecla == '-':
				if tecla == '*':
					entrada1.set(entrada2.get() + '*')
				elif tecla == '/':
					entrada1.set(entrada2.get() + '/')
				elif tecla == '+':
					entrada1.set(entrada2.get() + '+')
				elif tecla == "-":
					entrada1.set(entrada2.get() + '-')

				entrada2.set('')

			if tecla == '=':
				entrada1.set(entrada1.get() + entrada2.get())
				resultado = eval(entrada1.get())
				entrada2.set(resultado)

		self.ventana = tk.Toplevel()
		self.ventana.title('Calculadora')
		self.ventana.geometry('+500+80')
		self.ventana.columnconfigure(0,weight=1)
		self.ventana.rowconfigure(0,weight=1)
		
		stilos = ttk.Style()
		stilos = ttk.Style()
		stilos.theme_use('clam')
		stilos.configure('mainframe.TFrame',background="#DBDBDB")


		mainframe = ttk.Frame(self.ventana,style="mainframe.TFrame")
		mainframe.grid(column=0,row=0,columnspan=4,sticky=(W,N,E,S))
		mainframe.columnconfigure(0,weight=1)
		mainframe.columnconfigure(1,weight=1)
		mainframe.columnconfigure(2,weight=1)
		mainframe.columnconfigure(3,weight=1)

		mainframe.rowconfigure(0,weight=1)
		mainframe.rowconfigure(1,weight=1)
		mainframe.rowconfigure(2,weight=1)
		mainframe.rowconfigure(3,weight=1)
		mainframe.rowconfigure(4,weight=1)
		mainframe.rowconfigure(5,weight=1)
		mainframe.rowconfigure(6,weight=1)
		mainframe.rowconfigure(7,weight=1)




		stilos_Labe1 = ttk.Style()
		stilos_Labe1.configure('Label1.TLabel',font='arial 15',anchor='e')

		stilos_Labe2 = ttk.Style()
		stilos_Labe2.configure('Label2.TLabel',font='arial 40',anchor='e')

		stilos_botones_numero = ttk.Style()
		stilos_botones_numero.configure('Botones_numero.TButton',font='arial 22',width=5,background='#FFFFFF',relief='flat')
		stilos_botones_numero.map('Botones_numero.TButton',background=[('active','#B9B9B9')])

		stilos_botones_borrar = ttk.Style()
		stilos_botones_borrar.configure('Botones_borrar.TButton',font='arial 22',width=5,relief='flat',background='#CECECE')
		stilos_botones_borrar.map('Botones_borrar.TButton',foreground=[('active','#FF0000')],background=[('active','#CECECE')])


		stilos_botones_restantes = ttk.Style()
		stilos_botones_restantes.configure('Botones_restantes.TButton',font='arial 22',width=5,relief='flat',background='#CECECE')
		stilos_botones_restantes.map('Botones_restantes.TButton',background=[('active','#858585')])


		entrada1 = StringVar()
		pantalla = ttk.Label(mainframe,textvariable=entrada1,style='Label1.TLabel')
		pantalla.grid(column=0,row=0,columnspan=4,sticky=(W,N,E,S))

		entrada2 = StringVar()
		pantalla2 = ttk.Label(mainframe,textvariable=entrada2,style='Label2.TLabel')
		pantalla2.grid(column=0,row=1,columnspan=4,sticky=(W,N,E,S))

		button0 = ttk.Button(mainframe,text='0',style='Botones_numero.TButton',command=lambda:ingresarValores('0'))
		
		button1 = ttk.Button(mainframe,text='1',style='Botones_numero.TButton',command=lambda:ingresarValores('1'))
		
		button2 = ttk.Button(mainframe,text='2',style='Botones_numero.TButton',command=lambda:ingresarValores('2'))
		
		button3 = ttk.Button(mainframe,text='3',style='Botones_numero.TButton',command=lambda:ingresarValores('3'))
		
		button4 = ttk.Button(mainframe,text='4',style='Botones_numero.TButton',command=lambda:ingresarValores('4'))
		
		button5 = ttk.Button(mainframe,text='5',style='Botones_numero.TButton',command=lambda:ingresarValores('5'))
		
		button6 = ttk.Button(mainframe,text='6',style='Botones_numero.TButton',command=lambda:ingresarValores('6'))
		
		button7 = ttk.Button(mainframe,text='7',style='Botones_numero.TButton',command=lambda:ingresarValores('7'))
		
		button8 = ttk.Button(mainframe,text='8',style='Botones_numero.TButton',command=lambda:ingresarValores('8'))
		
		button9 = ttk.Button(mainframe,text='9',style='Botones_numero.TButton',command=lambda:ingresarValores('9'))

		button_borrar = ttk.Button(mainframe,text=chr(9003),style='Botones_borrar.TButton',command=lambda:borrar())
		button_borrar_todo = ttk.Button(mainframe,text='C',style='Botones_borrar.TButton',command=lambda:borrar_todo())
		button_parentesis1 = ttk.Button(mainframe,text='(',style='Botones_restantes.TButton',command=lambda:ingresarValores('('))
		button_parentesis2 = ttk.Button(mainframe,text=')',style='Botones_restantes.TButton',command=lambda:ingresarValores(')'))
		button_punto = ttk.Button(mainframe,text='.',style='Botones_restantes.TButton',command=lambda:ingresarValores('.'))

		button_division = ttk.Button(mainframe,text=chr(247),style='Botones_restantes.TButton',command=lambda:ingresarValores('/'))
		button_multiplicacion = ttk.Button(mainframe,text='x',style='Botones_restantes.TButton',command=lambda:ingresarValores('*'))
		button_resta = ttk.Button(mainframe,text='-',style='Botones_restantes.TButton',command=lambda:ingresarValores('-'))
		button_suma = ttk.Button(mainframe,text='+',style='Botones_restantes.TButton',command=lambda:ingresarValores('+'))

		button_igual = ttk.Button(mainframe,text='=',style='Botones_restantes.TButton',command=lambda:ingresarValores('='))
		button_raiz_cuadrada = ttk.Button(mainframe,text='√',style='Botones_restantes.TButton',command=lambda:raizcuadradra())

		button_parentesis1.grid(column=0,row=2,sticky=(W,N,E,S))
		button_parentesis2.grid(column=1,row=2,sticky=(W,N,E,S))
		button_borrar_todo.grid(column=2,row=2,sticky=(W,N,E,S))
		button_borrar.grid(column=3,row=2,sticky=(W,N,E,S))

		button7.grid(column=0,row=3,sticky=(W,N,E,S))
		button8.grid(column=1,row=3,sticky=(W,N,E,S))
		button9.grid(column=2,row=3,sticky=(W,N,E,S))
		button_division.grid(column=3,row=3,sticky=(W,N,E,S))

		button4.grid(column=0,row=4,sticky=(W,N,E,S))
		button5.grid(column=1,row=4,sticky=(W,N,E,S))
		button6.grid(column=2,row=4,sticky=(W,N,E,S))
		button_multiplicacion.grid(column=3,row=4,sticky=(W,N,E,S))

		button1.grid(column=0,row=5,sticky=(W,N,E,S))
		button2.grid(column=1,row=5,sticky=(W,N,E,S))
		button3.grid(column=2,row=5,sticky=(W,N,E,S))
		button_suma.grid(column=3,row=5,sticky=(W,N,E,S))

		button0.grid(column=0,row=6,columnspan=2,sticky=(W,N,E,S))
		button_punto.grid(column=2,row=6,sticky=(W,N,E,S))
		button_resta.grid(column=3,row=6,sticky=(W,N,E,S))

		button_igual.grid(column=0,row=7,columnspan=3,sticky=(W,N,E,S))
		button_raiz_cuadrada.grid(column=3,row=7,sticky=(W,N,E,S))


		for child in mainframe.winfo_children():
			child.grid_configure(ipady=10,padx=1,pady=1)

		self.ventana.mainloop()
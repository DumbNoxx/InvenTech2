import tkinter as tk
from tkinter import *
from tkinter import font
import subprocess
import util.generic as util
from tkinter import messagebox
import os
from dotenv import load_dotenv


load_dotenv()
icon = os.getenv('ICON')

ventana_principal = tk.Tk()
util.centrar_ventana(ventana_principal,600,450)
ventana_principal.title('InvenTech Ventana Principal')

icon_1 = tk.PhotoImage(file=icon)

label = tk.Label(ventana_principal,text='Bienvenido a InvenTech',font=('Dyuthi',14))
label.pack(pady=30)
label = tk.Label(ventana_principal,text='\nApp para gestionar tu inventario, creado por NOXCOPORATIONS.CA',font=('Dyuthi',14))
label.pack()
label = tk.Label(ventana_principal,text='\nAplicacion creada sin fines de lucro.',font=('Dyuthi',14))
label.pack()
label = tk.Label(ventana_principal,text='\nEspero apoyen la app',font=('Dyuthi',14))
label.pack()


def iniciar_sesion():
	ventana_principal.destroy()
	subprocess.run(['python3','./main2.py'])

boton = tk.Button(ventana_principal,text='Iniciar Sesion',font=('Dyuthi',14),command=iniciar_sesion)
boton.pack(fill=tk.X,padx=15,pady=15)


def leave():
	resultado = messagebox.askquestion("Salir", '¿Estás seguro qué deseas salir?', icon='question', default='no')
	if resultado == 'yes':
		ventana_principal.destroy()

boton = tk.Button(ventana_principal,text='Salir',font=('Dyuthi',14),command=leave)
boton.pack(fill=tk.X,padx=15,pady=15)

copyright = tk.Label(ventana_principal,text='Nox Corporations ©',font=('Dyuthi',10))
copyright.place(x=480,y=400,relwidth=0.20,relheight=0.05)


ventana_principal.iconphoto(True,icon_1)
ventana_principal.mainloop()
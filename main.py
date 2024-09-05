import tkinter as tk
from tkinter import *
from tkinter import font
import subprocess

ventana_principal = tk.Tk()
ventana_principal.geometry('800x500')
ventana_principal.title('InvenTech Ventana Principal')

label = tk.Label(ventana_principal,text='Bienvenido a InvenTech',font=('Dyuthi',14))
label.pack(pady=30)
label = tk.Label(ventana_principal,text='\nApp para gestionar tu inventario, creado por NOXCOPORATION.CA',font=('Dyuthi',14))
label.pack()
label = tk.Label(ventana_principal,text='\nAplicacion creada sin fines de lucro.',font=('Dyuthi',14))
label.pack()
label = tk.Label(ventana_principal,text='\nEspero apoyen la app',font=('Dyuthi',14))
label.pack()


def iniciar_sesion():
	ventana_principal.destroy()
	subprocess.run(['python3','./main2.py'])

boton = tk.Button(ventana_principal,text='Iniciar Sesion',font=('Dyuthi',14),command=iniciar_sesion)
boton.pack()


ventana_principal.mainloop()
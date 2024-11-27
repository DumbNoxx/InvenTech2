#!usr/bin/env python3

import tkinter as tk
from tkinter import *
from tkinter import font
import util.generic as util
from tkinter import messagebox
from main import PantallaCarga
import customtkinter as ct
from PIL import Image

ventana_principal = tk.Tk()
util.centrar_ventana(ventana_principal,600,470)
ventana_principal.title('InvenTech Ventana Principal')
ventana_principal.resizable(width=0,height=0)
my_image = ct.CTkImage(light_image=Image.open("./resources/Icono_Rework-transformed.png"),
                                  dark_image=Image.open("./resources/Icono_Rework-transformed.png"),
                                  size=(600,230))
ventana_principal.config(bg='#222831')

icon_1 = tk.PhotoImage(file='./icons.ico')

label = ct.CTkLabel(ventana_principal,text='Bienvenido a InvenTech',font=('Dyuthi',18),fg_color='transparent',text_color='#EEEEEE')
label.pack(pady=30)
label = ct.CTkLabel(ventana_principal,text='\nApp para gestionar tu inventario, creado por NOXCOPORATIONS.CA',font=('Dyuthi',16),fg_color='transparent',text_color='#EEEEEE')
label.pack()
label = ct.CTkLabel(ventana_principal,text='\nAplicacion creada sin fines de lucro.',font=('Dyuthi',16),fg_color='transparent',text_color='#EEEEEE')
label.pack()
label = ct.CTkLabel(ventana_principal,text='\nEspero apoyen la app',font=('Dyuthi',16),fg_color='transparent',text_color='#EEEEEE')
label.pack()



def iniciar_sesion():
	ventana_principal.destroy()
	PantallaCarga()

boton = ct.CTkButton(ventana_principal,text='Iniciar',fg_color='#31363F',font=('Dyuthi',16),command=iniciar_sesion)
boton.pack(fill=tk.X,padx=15,pady=10)


def leave():
	resultado = messagebox.askquestion("Salir", '¿Estás seguro qué deseas salir?', icon='question', default='no')
	if resultado == 'yes':
		ventana_principal.destroy()

boton = ct.CTkButton(ventana_principal,text='Salir',font=('Dyuthi',16),fg_color='#31363F',bg_color='#31363F',command=leave)
boton.pack(fill=tk.X,padx=15,pady=10)

frame_fill = tk.Frame(ventana_principal,height=20,width=5,bd=0,relief=tk.SOLID,bg='#222831')
frame_fill.pack(side='bottom',expand=tk.YES,fill=tk.BOTH)
copyright = ct.CTkLabel(frame_fill,text='Nox Corporations ©',font=('Dyuthi',10),bg_color='#222831',fg_color='#222831',text_color='#EEEEEE')
copyright.pack()

label_logo = ct.CTkLabel(frame_fill,text='',image=my_image,fg_color='transparent',bg_color='#222831')
label_logo.pack(padx=0.01,pady=0.01)

ventana_principal.iconphoto(True,icon_1)

ventana_principal.mainloop()

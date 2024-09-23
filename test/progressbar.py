#!/usr/bin/env python3
from tkinter import *
from tkinter.ttk import *
import tkinter as tk
import time

ventana = tk.Tk()
ventana.title('Cargando')
ventana.resizable(width=0,height=0)
ventana.geometry('400x350')
task = 100
x = 0
bar = Progressbar(ventana,orient=tk.HORIZONTAL,length=350)
bar.pack(padx=10,pady=10)
porcentaje = StringVar()
while(x<task):
	time.sleep(1)
	bar['value']+=1
	x+=1
	percent = tk.Label(ventana,text=f'{int((x/task)*100)}%')
	percent.place(x=140,y=50)
	ventana.update()
	ventana.after(600,percent.destroy)
	

if x == task:
	time.sleep(0.5)
ventana.destroy()
#!usr/bin/env python3

from tkinter import ttk
import tkinter as tk
import util.generic as util

class AdminWindowDesigner:

	def __init__(self):
		self.ventana = tk.Tk()
		self.ventana.title('Admin')
		self.ventana.config(bg='red')
		self.ventana.resizable(width=0,height=0)
		util.centrar_ventana(self.ventana,800,600)

		boton_leave = tk.Button(self.ventana,text='Leave',command=self.leave)
		boton_leave.pack()
		boton_leave.bind('<Return>',(lambda event:self.leave()))

		self.ventana.mainloop()


if __name__ == '__main__':
	AdminWindowDesigner()


def leave():
	pass
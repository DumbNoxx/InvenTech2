import tkinter as tk
from tkinter.font import BOLD
import util.generic as util

class MasterPanel:
	def __init__(self):
		self.ventana = tk.Tk()
		self.ventana.title('InvenTech')
		w,h = self.ventana.winfo_screenwidth(),self.ventana.winfo_screenheight()
		self.ventana.geometry("%dx%d+0+0" % (w,h))
		self.ventana.config(bg='#09ab53')
		self.ventana.resizable(width=0,height=0)

		logo = util.leer_image('./resources/logo.png',(200,200))

		label1 = tk.Label(self.ventana,image=logo,bg='#91a499')
		label1.place(x=0,y=0,relwidth=1,relheight=1)

		self.ventana.mainloop()
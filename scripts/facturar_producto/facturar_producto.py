#!/usr/bin/env python3
from scripts.facturar_producto.facturar_producto_designer import FacturarProductDesginer
import tkinter as tk

class FacturarProductCreate(FacturarProductDesginer):
	def __init__(self):
		super().__init__()

	def leave(self):
		self.ventana.destroy()

if __name__ == '__main__':
	FacturarProductCreate()
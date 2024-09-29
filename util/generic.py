#!/usr/bin/env python3
from PIL import Image, ImageTk

def leer_image(path,size):
	return ImageTk.PhotoImage(Image.open(path).resize(size,Image.Resampling.LANCZOS))


def centrar_ventana(ventana,aplicacion_ancho,aplicacion_largo):
	pantall_ancho = ventana.winfo_screenwidth()
	pantall_largo = ventana.winfo_screenheight()
	x = int((pantall_ancho/2)-(aplicacion_ancho/2))
	y = int((pantall_largo/2) - (aplicacion_largo/2))
	return ventana.geometry(f'{aplicacion_ancho}x{aplicacion_largo}+{x}+{y}')
	

from form.register.form_designer import FormRegisterDesigner
from persistence.repository.auth_user_repository import AuthUserRepository
from persistence.model import Auth_user
from tkinter import messagebox
import util.encoding_uncoding as end_dec
import tkinter as tk

class FormRegister(FormRegisterDesigner):


	def __init__(self):
		self.auth_repository = AuthUserRepository()
		super().__init__()
		
	def leave(self):
			resultado = messagebox.askquestion("Salir", '¿Estás seguro que quieres salir de la ventana?', icon='question', default='no')
			if resultado == 'yes':
				self.ventana.destroy()


	def register(self):
		if(self.isConfimationPassword()):
			user = Auth_user()
			user.username = self.usuario.get()
			user_db:Auth_user = self.auth_repository.getUserByUserName(self.usuario.get())
			
			if not (self.isUserRegister(user_db)):
				user.password = end_dec.encrypted(self.password.get())
				self.auth_repository.insertUser(user)
				messagebox.showinfo(
					message=f'Usuario "{self.usuario.get()}" registrado satisfactoriamente',title='Registro de Usuario')
				self.ventana.destroy()
		



	def isConfimationPassword(self):
		status:bool = True
		if(self.password.get() != self.confirmation.get()):
			status = False
			messagebox.showerror(
				message='Las contraseñas no coinciden, por favor verifica el registro',title='Error al registrar' )
			self.password.delete(0,tk.END)
			self.confirmation.delete(0,tk.END)
		return status

	def isUserRegister(self,user:Auth_user):
		status:bool = False
		if(user != None):
			status = True
			messagebox.showerror(
				message='El usuario ya existe',title='Error al registrar')
		return status

if __name__ == '__main__':
	FormRegister()
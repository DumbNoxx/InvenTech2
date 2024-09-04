import tkinter as tk
from tkinter import ttk,messagebox
from tkinter.font import BOLD
import util.generic as util
from form.master.form_master import MasterPanel
from form.login.form_login_designer import FormLoginDesigner
from persistence.model import Auth_user
import util.encoding_uncoding as end_dec
from persistence.repository.auth_user_repository import AuthUserRepository
from form.register.form import FormRegister

class FormLogin(FormLoginDesigner):
	def __init__(self):
		self.auth_repository = AuthUserRepository()
		super().__init__()

	def verificar(self):
		user_db:Auth_user = self.auth_repository.getUserByUserName(self.usuario.get())
		if(self.isUser(user_db)):
			self.isPassword(self.password.get(),user_db)


	def userRegister(self):
		FormRegister().mainloop()

	def isUser(self,user:Auth_user):
		status:bool = True
		if(user == None):
			status = False
			messagebox.showerror(
				message='El usuario no existe, por favor registrese',title='Error',parent=self.ventana)
		return status

	def isPassword(self,password:str,user:Auth_user):
		b_password = end_dec.decrypt(user.password)
		if(password == b_password):
			self.ventana.destroy()
			MasterPanel()
		else:
			messagebox.showerror(
			message='La contraseña no es correcta',title='Error')	
	
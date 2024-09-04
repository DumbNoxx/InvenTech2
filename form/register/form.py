from form.register.form_designer import FormRegisterDesigner
from persistence.repository.auth_user_repository import AuthUserRepository
from persistence.model import Auth_user
from tkinter import messagebox
import util.encoding_uncoding as end_dec
import tkinter as tk

class FormRegister(FormRegisterDesigner):
	def __init__(self):
		super().__init__()
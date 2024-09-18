from scripts.ver_productos.ver_productos_designer import VerProductosDesigner
from persistence.repository.auth_user_repository import AuthUserRepository
from persistence.model import Inventary
import tkinter as tk
from tkinter import ttk
from sqlalchemy.orm import Session
import sqlalchemy as db

class VerProductosCreate(VerProductosDesigner):

	def __init__(self):
		super().__init__()


import tkinter as tk
from tkinter import font


root = tk.Tk()
for font in font.families():
    print(font)
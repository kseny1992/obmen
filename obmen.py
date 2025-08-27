import requests
import json
from tkinter import *
from tkinter import messagebox as mb

from PyInstaller.loader.pyiboot01_bootstrap import entry

def exchange():


window = Tk()
window.title("курсы обмена валют")
window.geometry("360x180")

Label(text="ВВЕДИТЕ КОД ВАЛЮТЫ").pack(padx=10,pady=10)

entry = Entry()
entry.pack(padx=10,pady=10)

Button(text="Получить курс обмена к доллару", command=exchange).pack(padx=10,pady=10)

window.mainloop()


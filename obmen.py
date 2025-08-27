import requests
import json
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk

from bottle import response


def exchange():
    #code = entry.get()
    code = combobox.get()
    if code:
        try:
            response = requests.get('https://open.er-api.com/v6/latest/USD')
            response.raise_for_status()
            data = response.json()
            if code in data ['rates']:
                exchange_rate = data['rates'][code]
                mb.showinfo('Курс обмена', f'Курс:{exchange_rate:.2f} {code} за 1 доллар')
            else:
                mb.showerror("Ошибка",f'Валюта {code} не найдена')
        except Exception as e:
            mb.showerror("Ошибка",f"Произошла ошибка:{e}.")
    else:
        mb.showwarning("Внимание!","Введите код валюты") #ПРЕДУПРЕЖДЕНИЕ


window = Tk()
window.title("курсы обмена валют")
window.geometry("360x180")

Label(text="ВЫБЕРИТЕ КОД ВАЛЮТЫ").pack(padx=10,pady=10)

cur = ['RUB', 'EUR', 'GBP', 'JPY', 'CNY', 'KZT', 'UZS', 'CHF', 'AED', 'CAD'] #СПИСОК ОСНОВНЫХ ВАЛЮТ
combobox = ttk.Combobox(values=cur)
combobox.pack(padx=10,pady=10)

#entry = Entry()
#entry.pack(padx=10,pady=10)

Button(text="Получить курс обмена к доллару", command=exchange).pack(padx=10,pady=10)



window.mainloop()


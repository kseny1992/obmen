import requests
import json
from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
from bottle import response


def update_c_label(event):
    code = combobox.get()
    name = cur[code]
    c_label.config(text=name)

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
                c_name = cur[code]
                mb.showinfo('Курс обмена', f'Курс:{exchange_rate:.2f} {c_name} за 1 доллар')
            else:
                mb.showerror("Ошибка",f'Валюта {code} не найдена')
        except Exception as e:
            mb.showerror("Ошибка",f"Произошла ошибка:{e}.")
    else:
        mb.showwarning("Внимание!","Введите код валюты") #ПРЕДУПРЕЖДЕНИЕ

cur = {'RUB':'Poccийский рубль',
       'EUR':'Евро',
       'GBP':'Британский фунт стерлингов',
       'JPY':'Японская йена',
       'CNY':'Китайский юань',
       'KZT':'Казахский тенге',
       'UZS':'Узбекский сум',
       'CHF':'Швейцарский франк',
       'AED':'Дирхам ОАЭ',
       'CAD':'Канадский доллар'
       } #СПИСОК ОСНОВНЫХ ВАЛЮТ

window = Tk()
window.title("курсы обмена валют")
window.geometry("360x180")

Label(text="ВЫБЕРИТЕ КОД ВАЛЮТЫ").pack(padx=10,pady=10)

#cur = ['RUB', 'EUR', 'GBP', 'JPY', 'CNY', 'KZT', 'UZS', 'CHF', 'AED', 'CAD'] #СПИСОК ОСНОВНЫХ ВАЛЮТ
combobox = ttk.Combobox(values=list(cur.keys()))
combobox.pack(padx=10,pady=10)
combobox.bind("<<ComboboxSelected>>",update_c_label)
#entry = Entry()
#entry.pack(padx=10,pady=10)

c_label = ttk.Label()
c_label.pack(padx=10,pady=10)


Button(text="Получить курс обмена к доллару", command=exchange).pack(padx=10,pady=10)



window.mainloop()


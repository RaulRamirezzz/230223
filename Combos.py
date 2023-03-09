from tkinter import *
from tkinter import ttk

raiz = Tk()

color=StringVar()

comboColor = ttk.Combobox(raiz, textvariable=color)
comboColor.grid()
comboColor['values'] = ("Rojo", "Azul", "Verde", "Amarillo", "Rosa", "Morado")

raiz.mainloop()

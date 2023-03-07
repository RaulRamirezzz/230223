'''
Raul Antonio Ramirez Mendez
Inicio de sesion usando TKINTER
03 de Marzo del 2023
ttk
'''

from tkinter import *
from tkinter import ttk

class Login:
    
    #Constructor de la clase
    def __init__(self, raiz):
        raiz.title('INICIO DE SESION')
        
        self.usuario = StringVar()
        self.contrasena = StringVar()
        
        mainFrame=ttk.Frame(raiz, padding="20 30 20 30")#Padding establece margen(Izquierda, arriba, derecha, abajo)
        mainFrame.grid(column=0, row=0)
        
        usuarioEntry=ttk.Entry(mainFrame, width=40 ,textvariable=self.usuario)
        usuarioEntry.grid(column=2,row=1,)
        contrasenaEntry=ttk.Entry(mainFrame, width=40 ,textvariable=self.contrasena)
        contrasenaEntry.grid(column=2,row=3)
        
        ttk.Label(mainFrame, text="Usuario: ").grid(column=1, row=1)
        ttk.Label(mainFrame, text="").grid(column=1, row=2)
        ttk.Label(mainFrame, text="Contrasena: ").grid(column=1, row=3) 
        ttk.Label(mainFrame, text="").grid(column=1, row=4)
        
        ttk.Button(mainFrame, text="Ingresar").grid(column=2, row=5, sticky=(E))#, command=self.ingresar
        
        usuarioEntry.focus()#Inicia en ese campo
        raiz.bind("<Return>", contrasenaEntry.focus())

    
raiz= Tk()
Login(raiz)
raiz.mainloop()
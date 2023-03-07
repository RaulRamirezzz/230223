'''
Raul Antonio Ramirez Mendez
App para convertir pies a metros usando TKINTER
23 de Febrero del 2023
ttk
'''

from tkinter import *
from tkinter import ttk

class Conversor:
    
    #Constructor de la clase
    def __init__(self, raiz):
        raiz.title('Pies a metros')
        
        self.pies = StringVar()
        self.metros = StringVar()
        
        mainFrame=ttk.Frame(raiz, padding="3 3 12 12")#Padding establece margen(Izquierda, arriba, derecha, abajo)
        mainFrame.grid(column=0, row=0)
        
        piesEntry=ttk.Entry(mainFrame, width=7 ,textvariable=self.pies)
        piesEntry.grid(column=2,row=1)
        
        ttk.Label(mainFrame, text="Pies").grid(column=3, row=1)#Sticky=(E)Se usa para cambiar de direccion
        ttk.Label(mainFrame, text="Son equivalentes a: ", padding=(5, 10, 5, 10)).grid(column=1, row=2)
        ttk.Label(mainFrame, textvariable=self.metros).grid(column=2, row=2)
        ttk.Label(mainFrame, text="Metros").grid(column=3, row=2)
        
        ttk.Button(mainFrame, text="Calcular", command=self.calcular).grid(column=3, row=3)
        
        piesEntry.focus()#Inicia en ese campo
        #Hacer la operacion presionando enter
        raiz.bind("<Return>", self.calcular)

    def calcular(self, *args):
        print("Boton presionado")
        pieUsuario = self.pies.get()
        try:
            piesFlotante = float(pieUsuario)
            metros = piesFlotante * 0.3048
            print("Metros: ", metros)
            self.metros.set(metros)
            
        except ValueError:
            print("No es un dato valido")
            self.pies.set("")#Vacia el campo
    
if __name__ == "__main__":
    print('Este es el archivo principal')
    print('Nadamas se mostrar si esto es el archivo principal')
    

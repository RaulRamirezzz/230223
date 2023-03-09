from tkinter import *
from tkinter import ttk

raiz=Tk()
raiz.title('Muestra Widgets')

nombre = StringVar()
aPaterno = StringVar()
aMaterno = StringVar()
correo = StringVar()
movil = StringVar()

mainFrame=ttk.Frame(raiz, padding="20 30 20 30", relief="raised")
mainFrame.grid(column=0, row=0)

        
nombreEntry=ttk.Entry(mainFrame, width=40 ,textvariable=nombre)
nombreEntry.grid(column=2,row=1,)
aPaternoEntry=ttk.Entry(mainFrame, width=40 ,textvariable=aPaterno)
aPaternoEntry.grid(column=2,row=3)
aMaternoEntry=ttk.Entry(mainFrame, width=40 ,textvariable=nombre)
aMaternoEntry.grid(column=2,row=5)
correoEntry=ttk.Entry(mainFrame, width=40 ,textvariable=aPaterno)
correoEntry.grid(column=2,row=7)
movilEntry=ttk.Entry(mainFrame, width=40 ,textvariable=nombre)
movilEntry.grid(column=2,row=9)
        
ttk.Label(mainFrame, text="Nombre: ").grid(column=1, row=1)
ttk.Label(mainFrame, text="").grid(column=1, row=2)
ttk.Label(mainFrame, text="A.Paterno: ").grid(column=1, row=3) 
ttk.Label(mainFrame, text="").grid(column=1, row=4)
ttk.Label(mainFrame, text="A.Materno: ").grid(column=1, row=5)
ttk.Label(mainFrame, text="").grid(column=1, row=6)
ttk.Label(mainFrame, text="Correo: ").grid(column=1, row=7) 
ttk.Label(mainFrame, text="").grid(column=1, row=8)
ttk.Label(mainFrame, text="Movil: ").grid(column=1, row=9)
ttk.Label(mainFrame, text="").grid(column=1, row=10)


aficiones=ttk.Frame(raiz, padding="80 30 80 30", relief="raised")
aficiones.grid(column=0, row=1, pady=20)
rbleer = ttk.Checkbutton(aficiones, text='Leer')
rbmusica = ttk.Checkbutton(aficiones, text='Leer')
rbvideojuegos = ttk.Checkbutton(aficiones, text='Leer')
ttk.Label(aficiones, text="Aficiones: ").grid(column=0, row=0)
rbleer.grid(column=0, row=1, padx=10, pady=5)
rbmusica.grid(column=1, row=1, padx=10, pady=5)
rbvideojuegos.grid(column=2, row=1, padx=10, pady=5)



terminar=ttk.Frame(raiz, padding="20 30 20 30")
terminar.grid(column=0, row=2)
ttk.Button(terminar, text="Guardar").grid(column=1, row=0, padx=50)
ttk.Button(terminar, text="Cancelar").grid(column=3, row=0)


dedicacion=ttk.Frame(raiz, padding="20 30 20 30")
dedicacion.grid(column=1, row=0)
rbestudiante = ttk.Radiobutton(dedicacion, text='Estudiante')
rbempleado = ttk.Radiobutton(dedicacion, text='Empleado')
rbdesempleado = ttk.Radiobutton(dedicacion, text='Desempleado')

rbestudiante.grid(column=0, row=0, padx=10, pady=5)
rbempleado.grid(column=0, row=1, padx=10, pady=5)
rbdesempleado.grid(column=0, row=2, padx=10, pady=5)

estado=ttk.Frame(raiz, padding="20 30 20 30")
estado.grid(column=1, row=1)
estados=StringVar()
comboEstados = ttk.Combobox(estado, textvariable=estado)
comboEstados.grid()
comboEstados['values'] = ("Jalisco", "Sinaloa", "Michoacan", "CDMX")

raiz.mainloop()
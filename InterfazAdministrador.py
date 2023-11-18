from tkinter import*

#Se usan los comandos basicos para crear botones en tkinter, cuadros de texto y la ventana principal de la app

def interfaz():
    root = Tk()

    root.geometry("900x480")
    root.title("Proyecto Administrador de Archivos")
    root.resizable(0,0)

    boton1 = Button(root, text="Crear Archivos")
    boton1.place(x=330,y=280)

    boton2 = Button(root, text="Crear Directorio")
    boton2.place(x=440,y=280)

    boton3 = Button(root, text="Eliminar Archivo")
    boton3.place(x=550,y=280)

    boton4 = Button(root, text="Eliminar Directorio")
    boton4.place(x=670,y=280)

    boton5 = Button(root, text="Renombrar Archivo")
    boton5.place(x=330,y=330)

    boton6 = Button(root, text="Renombrar Directorio")
    boton6.place(x=460,y=330)

    boton7 = Button(root, text="Mostrar Arbol de Directorios")
    boton7.place(x=610,y=330)

    boton8 = Button(root, text="Salir", command=exit)
    boton8.place(x=850,y=440)

    texto = Text()
    texto.place (x=5, y=40 , width=200, height=400)
    
    texto2 = Text()
    texto2.place(x=230, y=50 , width=650, height=200)

    root.mainloop()
    
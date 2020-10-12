# Modulo para crear interfacer graficas
from tkinter import *

class Program():

    ventana = Tk()
    title = "Mi Primer Programa Con Tkinter - By En8oy"
    size = "1080x720"
    path_icon = "./img/logo.ico"
    resizable = False

    def __init__(self):
        # Crear una ventana raiz
        # Titulo del programa
        self.ventana.title(self.title)
        # Tamaño de programa
        self.ventana.geometry(self.size)
        # Icono de la aplicación
        self.ventana.iconbitmap("./img/logo.ico")
        # Bloquea la redimencion
        if self.resizable:
            self.ventana.resizable(1,1)
        else:
            self.ventana.resizable(0,0)

    def body(self):
        # Orientadores en python son las siguientes 
        #     nw = noroeste
        #     n =  norte
        #     ne = noroeste
        #     w = oeste
        #     center = centro
        #     e = este
        #     sw = 
        #     s = 
        #     se = 
        txt = Label(self.ventana, text="Hola Mundo Desde El Body")
        txt.config(
            fg = "white",
            bg = "#303030",
            padx = "50",
            pady = "50",
            font = ("Arial", 20)
        )
        txt.pack()

    def create(self):
        self.ventana.mainloop()

program = Program()
program.body()
program.create()




# Arranca la ventana
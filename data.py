from tkinter import *
from tkinter.messagebox import *

import sqlite3

def go_home():
    pass

def cerrar():
    pass

def dbconsult(var):
    db = sqlite3.connect('admin')
    cursor = db.cursor()
    f = cursor.execute("SELECT * FROM usuarios WHERE Nombre = '%s'"%(var))
    fila = f.fetchone()

    print(fila)

    if (fila != None):
        titulo_ = Label(ventana_home, text= "Resultados")
        contenedor1 = Label(ventana_home, text="1. cedula: %s"%fila[0])
        contenedor2 = Label(ventana_home, text="2. Nombre: %s"%fila[1])
        contenedor3 = Label(ventana_home, text="3. Apellido: %s"%fila[2])
        contenedor4 = Label(ventana_home, text="4. Cargo: %s"%fila[3])

        titulo_.grid(row=2, column=2, pady=5, sticky="W")
        contenedor1.grid(row=3, column=2, sticky="W")
        contenedor2.grid(row=4, column=2, sticky="W")
        contenedor3.grid(row=5, column=2, sticky="W")
        contenedor4.grid(row=6, column=2, sticky="W")
    else:
        showerror("Ups, algo salio mal", "No se encontró el registro")

def consultar(valor):
    valor = valor.capitalize()
    dbconsult(valor)

def home():
    global ventana_home
    global entrada
    ventana_home = Tk()
    ventana_home.title("Home")
    ventana_home.geometry("350x320+500+250")

    new_menu = Menu(ventana_home)
    ventana_home.config(menu=new_menu)

    #Crate a menu item
    file_menu = Menu(new_menu)
    new_menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Home", command=go_home)
    file_menu.add_command(label="Cerrar sesión", command=cerrar)
    file_menu.add_command(label="Salir", command=quit)

    dato = StringVar()

    titulo = Label(ventana_home, text="CONTACTOS", anchor="n", font="verdana 10 bold")
    etiqueta = Label(ventana_home, text="Nombre:")
    entrada = Entry(ventana_home, width= 20)
    boton = Button(ventana_home, text="Consultar", command=lambda:consultar(entrada.get()))

    titulo.grid(row=0, column=2, padx=10)
    etiqueta.grid(row=1, column=1, padx=5)
    entrada.grid(row=1, column=2, padx=10)
    boton.grid(row=1, column=3, pady=10)

    ventana_home.mainloop()
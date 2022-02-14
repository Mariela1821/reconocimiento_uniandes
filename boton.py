import sqlite3
from tkinter import *
from tkinter import ttk
conexion = sqlite3.connect('admin.db')
cursor = conexion.execute("SELECT id,Nombre, Permiso from admin")
for fila in cursor:
    print(fila)
    conexion.close()

def ingresar():
    cursor.execute(
                f"INSERT INTO usuarios(nacionalidad, cedula, Nombre, Apellido, Direccion, Contra)VALUES({naci},{ci},{Nombre},{Apellido},{Direccion});")
    conexion.commit()
def modi():
    cursor.execute(
                f"UPDATE usuarios(nacionalidad, cedula, Nombre, Apellido, Direccion, Contra)VALUES({naci},{ci},{Nombre},{Apellido},{Direccion});")
    conexion.commit()
def eliminar():
    cursor.execute(
                f"DELETE FROM usuarios WHERE id={}")
    conexion.commit()

def guardar():
    pass
def cancelar():
    pass
root = Tk()
root.geometry('650x558+320+0')
frame =Frame(root)
frame=Frame(root, bg="#bfdaff")
frame.place(x=0, y = 0, width=100, height=558)

frame.pack
frame.config(bg="lightblue")
frame.config(width=480, height=320)
bot1=Button(frame, text="Nuevo", command=ingresar, bg="blue", fg="white")
bot1.place(x=5, y =50, width=80, height=30)
bot2=Button(frame, text="Modificar", command=modi, bg="blue", fg="white")
bot2.place(x=5, y =100, width=80, height=30)
bot3=Button(frame, text="Eliminar", command=eliminar, bg="blue", fg="white")
bot3.place(x=5, y =150, width=80, height=30)

frame1=Frame(root, bg="#d3dde3")
frame1.place(x=95, y=0, width=150, height=558)
lbl=Label(frame1, text='Usuario: ',font=('Arial Black', 12))
lbl.place(x=3,y=10)
txtusu=Entry(frame1)
txtusu.place(x=3, y = 50)
lbl1=Label(frame1, text='Fecha: ',font=('Arial Black', 12))
lbl1.place(x=3,y=90)
txtusu=Entry(frame1)
txtusu.place(x=3, y = 130)
bot2=Button(frame1, text="Guardar", command=guardar, bg="blue", fg="white")
bot2.place(x=10, y =210, width=60, height=30)
bot3=Button(frame1, text="Cancelar", command=cancelar, bg="blue", fg="white")
bot3.place(x=80, y =210, width=60, height=30)

gri=ttk.Treeview(root, columns=("col1", "col2", "col3"))
gri.column("#0", width=50)
gri.column("col1", width=60, anchor=CENTER)
gri.column("col2", width=90, anchor=CENTER)
gri.column("col3", width=90, anchor=CENTER)

gri.heading("#0", text="ID",anchor=CENTER)
gri.heading("col1",text="Usuario", anchor=CENTER)
gri.heading("col2",text="Fecha", anchor=CENTER)
#gri.heading("col3",text="ID", anchor=CENTER)

gri.place(x=247, y =0, width=400, height=250)

gri.insert("", END, text="1", values=("Fernanda", "14/2/2022"))



root.mainloop()




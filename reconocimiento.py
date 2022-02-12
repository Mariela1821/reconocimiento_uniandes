from playsound import playsound 
import pathlib
from email import message
from select import select
from tkinter import*
import sqlite3
import tkinter as tk
from tkinter import messagebox
import sqlite3
from tkinter import *
import tkinter as tk
from turtle import left
from PIL import Image, ImageTk
from tkinter import messagebox as mb
import cv2
import os
import imutils
from matplotlib import image
from numpy import *
import numpy as np
import time
from PIL import Image
import sqlite3
import xml.etree.ElementTree
#from PIL import Image, ImageTk
import datetime
db = sqlite3.connect('admin.db')
c = db.cursor()
permiso = ''
getName = ''
def rostro(Nombre):
    # global getName
    personName = Nombre
    dataPath = 'data'
    personPath = dataPath + '/' + personName
    if not os.path.exists(personPath):
        print('Carpeta creada: ', personPath)
        os.makedirs(personPath)
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
#cap = cv2.VideoCapture('Video.mp4')
    faceClassif = cv2.CascadeClassifier(
        'haarcascades/haarcascade_frontalface_default.xml')
    count = 0

    while True:

        ret, frame = cap.read()
        if ret == False:
            break
        frame = imutils.resize(frame, width=640)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        auxFrame = frame.copy()

        faces = faceClassif.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
            rostro = auxFrame[y:y+h, x:x+w]
            rostro = cv2.resize(rostro, (150, 150),
                                interpolation=cv2.INTER_CUBIC)
            cv2.imwrite(personPath + '/rotro_{}.jpg'.format(count), rostro)
            count = count + 1
        cv2.imshow('frame', frame)

        k = cv2.waitKey(1)
        if k == 27 or count >= 100:
            break

    cap.release()
    cap.release()
    cv2.destroyAllWindows()
def entrenador():
	dataPath = 'data'
	peopleList = os.listdir(dataPath)
	print('Lista de personas: ', peopleList)
	  
	labels = []
	facesData = []
	label = 0

	for nameDir in peopleList:
		personPath = dataPath + '/' + nameDir
		print( 'Leyendo las imagenes:' ,personPath )

		for fileName in os.listdir(personPath):
			print('Rostros: ', nameDir + '/' + fileName)
			labels.append(label)
			facesData.append(cv2.imread(personPath+'/'+fileName,0))
			image = cv2.imread(personPath +'/'+ fileName,0)
			#cv2.imshow('image',image)
			#cv2.waitKey(10)
		label = label + 1
	face_recognizer = cv2.face.LBPHFaceRecognizer_create()
	print("Entrenando..")
	face_recognizer.train(facesData, np.array(labels))
	face_recognizer.save('modelLBPHFace.xml')
	print("Modelo almacenado..")
	cv2.destroyAllWindows()
def reconocimiento():
    dataPath = ('data')
    imagePaths = os.listdir(dataPath)
    
    INSERT
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    # leyendo el modelo
    face_recognizer.read('modelLBPHFace.xml')

    cap = cv2.VideoCapture(0)
    #cap= cv2.VideoCapture('/home/pi/tomas/Mary.mp4')

    faceClassif = cv2.CascadeClassifier(
        'haarcascades/haarcascade_frontalface_default.xml')
    cont = 0
    while True:
        ret, frame = cap.read()
        if ret == False:
            break
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        auxFrame = gray.copy()

        faces = faceClassif.detectMultiScale(gray, 1.3, 5)
        dt = str(datetime.datetime.now()) 

        for (x, y, w, h) in faces:
            rotro = auxFrame[y:y+h, x:x+w]
            rotro = cv2.resize(rotro, (150, 150),interpolation=cv2.INTER_CUBIC)
            result = face_recognizer.predict(rotro)
            cv2.putText(frame, '{}'.format(result), (x, y-5),1, 1.3, (255, 255, 0), 1, cv2.LINE_AA)

            if result[1] < 80:
                cv2.putText(frame, '{}'.format(
                    imagePaths[result[0]]), (x, y-25), 2, 1.1, (0, 255, 0), 1, cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                RName = frame, '{}'.format(imagePaths[result[0]])
                global Resultado
                Resultado = RName[1]
                print("resultado", Resultado)
                if Resultado:
                    print('Ingreso Correcto')
                    print("entro")

                else:
                    print('usuario desconocido')
                    play
            else:
                cv2.putText(frame, 'Desconocido', (x, y-20), 2,
                            0.8, (0, 255, 0), 1, cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
                print("no se encontro coincidencias")

        if cont > 0:
            break
        cv2.imshow('frame', frame)
        k = cv2.waitKey(1)
        if k == 10:
            break

    cap.release()
    cv2.destroyAllWindows()
def play(): 
    print("Alerta Intruso")
    playsound('1.mp3') 
    cv2.destroyAllWindows()
def AdminUsu():
    Usu = tk.Toplevel(ventana)
    Usu.geometry('650x558+320+0')
    Usu.title('Administrador')
    ventana.configure(background='white')
    lab=Label(Usu,text="Administracion de Usuarios", font=("Cambria", 33), bg="#063970", fg="white", width="550", height="2")
    lab.pack()
  
def login():
    usuario = caja1.get()
    contra = caja2.get()
    c.execute('SELECT Permiso FROM admin WHERE Nombre = ? AND Contra = ?',
              (usuario, contra))
    permisoBol = False
    for i in c.fetchall():
        global permiso
        permiso = i[0]
        permisoBol = True
    if permisoBol:
        messagebox.showinfo(title='Login Correcto',
                            message='Usuario y contraseña correctos')
        menu()
        # reconocimiento(usuario)
    else:
        permiso = ''
        messagebox.showerror(title='Login incorrecto',
                             message='Usuario o contraseña incorrecto')
def nuevaventana():
    newVentana = tk.Toplevel(ventana)
    newVentana.geometry('650x558+320+0')
    newVentana.title('Registro de Usuario')
    ventana.configure(background='white')
    titulo=Label(newVentana,text="Registro de Usuario", font=("Cambria", 33), bg="#063970", fg="white", width="550", height="2")
    titulo.pack()
    ce=Label(newVentana, text='Cedula: ',font=('Arial Black', 12))
    ce.place(x=22,y=130)
    ce=StringVar()
    caja3 = Entry(newVentana,textvariable=ce, width="45")
    caja3.place(x=22, y=160)

    nom=Label(newVentana, text='Nombre: ',font=('Arial Black', 12))
    nom.place(x=22,y=190)
    nom=StringVar()
    caja4 = Entry(newVentana, textvariable=nom, width="45")
    caja4.place(x=22, y=220)

    ap=Label(newVentana, text='Apellido: ',font=('Arial Black', 12))
    ap.place(x=22,y=250)
    ap=StringVar()
    caja5 = Entry(newVentana,textvariable=ap, width="45")
    caja5.place(x=22,y=280)

    dir=Label(newVentana, text='Direccion: ',font=('Arial Black', 12))
    dir.place(x=22,y=310)
    dir=StringVar()
    caja6 = Entry(newVentana,textvariable=dir, width="45")
    caja6.place(x=22,y=340)
    
    contra=Label(newVentana, text='contraseña: ', font=('Arial Black', 12))
    contra.place(x=22,y=370)
    contra=StringVar()
    caja7 = Entry(newVentana, show='*',textvariable=contra, width="45")
    caja7.place(x=22,y=400)
    
    contrab=Label(newVentana, text='confirme contraseña: ', font=('Arial Black', 12))
    contrab.place(x=22,y=430)
    contrab=StringVar()
    caja8 = Entry(newVentana, show='*',textvariable=contrab, width="45")
    caja8.place(x=22,y=470)
    name = caja4.get()
    def registro():
        cedula = caja3.get()
        Nombre = caja4.get()
        Apellido = caja5.get()
        Cargo=caja6.get()
        ContraReg = caja7.get()
        ContraReg2 = caja8.get()
        if(ContraReg == ContraReg2):
            c.execute("INSERT INTO usuarios values(\'"+cedula+"\',\'" +
                      Nombre+"\',\'"+Apellido+"\',\'"+Cargo+"\',\'"+ContraReg+"')")
            db.commit()
            rostro(Nombre)
            entrenador()

            messagebox.showinfo(title='Registro correcto', message="Bienvenido " +
                                Nombre+" "+Apellido+" ¡¡ \n Su registro fu exitoso.")
        else:
            messagebox.showerror(title="Contraseña Incorrecta",
                                 message='Error¡¡¡ \n las contraseñas no coinciden.')

    buttons = tk.Button(newVentana, text='Registrar !', command=registro,bg="#063970", fg="white", width="30", height="2",font=('Arial Rounded MT Bold', 10))
    buttons.place(x=250, y=500)
def menu():
    menu = tk.Toplevel(ventana)
    menu.geometry('650x558+320+0')
    menu.title('Registro de Usuario')
    ventana.configure(background='white')
    barraMenu = Menu(ventana)
    mnuArchivo = Menu(ventana)
    mnuAdmin = Menu(ventana)
    mnuRepor = Menu(ventana)
    mnuSegu = Menu(ventana)
    mnuSalir = Menu(ventana)
# comandos
    mnuArchivo.add_command(label="Personas", command=nuevaventana)
    mnuArchivo.add_command(label="Cámaras", command= reconocimiento)
    mnuAdmin.add_command(label="Usuarios",command=AdminUsu)
    mnuRepor.add_command(label="Reportes", command=reportes)
    mnuSegu.add_command(label="Registro de usuarios", command=controlusuarios)
    mnuSegu.add_command(label="Cámaras", command=reconocimiento)
    #mnuSalir.add.command(label="Salir")

    global permiso
# mnuSalir.add_command(label="")
# nombres

    if(permiso == '1'):
        barraMenu.add_cascade(label="Registar", menu=mnuArchivo)
        barraMenu.add_cascade(label="Administrar", menu=mnuAdmin)
        barraMenu.add_cascade(label="Reportes", menu=mnuRepor)
        barraMenu.add_cascade(label="Seguridad", menu=mnuSegu)
        barraMenu.add_cascade(label="Salir", menu=mnuSalir)
        menu.config(menu=barraMenu)
    if(permiso == '2'):
        
        barraMenu.add_cascade(label="Administrar", menu=mnuAdmin)
        barraMenu.add_cascade(label="Reportes", menu=mnuRepor)
        barraMenu.add_cascade(label="Salir", menu=mnuSalir)
        menu.config(menu=barraMenu)
    if(permiso == '3'):
        barraMenu.add_cascade(label="Reportes", menu=mnuRepor)
        barraMenu.add_cascade(label="Seguridad", menu=mnuSegu)
        barraMenu.add_cascade(label="Salir", menu=mnuSalir)
        menu.config(menu=barraMenu)
    if(permiso == '4'):
        barraMenu.add_cascade(label="Reportes", menu=mnuRepor)
        barraMenu.add_cascade(label="Salir", menu=mnuSalir)
        menu.config(menu=barraMenu)
def controlusuarios():
    admin = tk.Toplevel(ventana)
    admin.geometry('650x558+320+0')
    admin.title('Administrador')
    ventana.configure(background='white')
    tit=Label(admin,text="Registro de Admin", font=("Cambria", 33), bg="#063970", fg="white", width="550", height="2")
    tit.pack()
    # ingreso de datos
    imagen=Image.open('admin.jpg')
    imagen= imagen.resize((280,200), Image.ANTIALIAS)
    photoImg=ImageTk.PhotoImage(imagen)
    panelReg=tk.Label(admin, image=photoImg).pack(side="left")
    dato=Label(admin, text='Nombre: ', font=('Arial Black', 12))
    dato.place(x=22, y=190)
    dato=StringVar
    caja10 = Entry(admin,textvariable=dato, width="45",highlightthickness=1)
    caja10.config(highlightbackground=color, highlightcolor=color)
    caja10.place(x=22, y=230)
    
    dato1=Label(admin, text='Contraseña: ', font=('Arial Black', 12))
    dato1.place(x=22, y= 270)
    dato1=StringVar
    caja11 = Entry(admin, textvariable=dato1,show='*',width="45",highlightthickness=1)
    caja11.config(highlightbackground=color, highlightcolor=color)
    caja11.place(x=22, y=310)

    dato2=Label(admin, text='Repita Contraseña: ', font=('Arial Black', 12))
    dato2.place(x=22, y=350)
    caja12=StringVar
    caja12 = Entry(admin, textvariable=dato2, show='*',width="45")
    caja12.config(highlightbackground=color, highlightcolor=color,highlightthickness=1)
    caja12.place(x=22, y=390)

    lblAnimo = Label(admin, text="Elija el permiso",font=('Arial Black', 12), bg="#1e81b0", fg="white", width="15", height="2")
    lblAnimo.place(x=400, y=130)
    select = IntVar()
    rdBAnimoE = Radiobutton(admin, text="Administrador", value=1,variable=select,font=("Cambria", 15))
    rdBAnimoE.place(x=400, y=190)
    rdBAnimoMB = Radiobutton(admin, text="Operador", value=2,variable=select,font=("Cambria", 15))
    rdBAnimoMB.place(x=400, y=230)
    rdBAnimoM = Radiobutton(admin, text="Usuario", value=3,variable=select,font=("Cambria", 15))
    rdBAnimoM.place(x=400, y=270)
    rdBAnimoB = Radiobutton(admin, text="SuperUsuario", value=4,variable=select,font=("Cambria", 15))
    rdBAnimoB.place(x=400, y=310)
    def registroamin():
        Nombre = caja10.get()
        Contraa = caja11.get()
        Contrab = caja12.get()
        admins = select.get()
        if(Contraa == Contrab):
            
            c.execute(
                f"INSERT INTO admin (Nombre, Contra,Permiso)values('{Nombre}', '{Contraa}', '{str(admins)}');")
            db.commit()
            messagebox.showinfo(
                title='Registro correcto', message="Bienvenido "+Nombre+" ¡¡ \n Su registro fu exitoso.")
            admin.destroy()
        else:
            messagebox.showerror(title="Contraseña Incorrecta",
                                 message='Error¡¡¡ \n las contraseñas no coinciden.')
    bottons = Button(admin,text='Registrar !', bg="#1e81b0",command=registroamin,width="20", height="2", fg="white",font=('Arial Black', 12))
    bottons.place(x=400, y=350)
def reportes():
    #print("este es el", Resultado)
    Repo = tk.Toplevel(ventana)
    Repo.geometry('650x558+320+0')
    Repo.title('Administrador')
    ventana.configure(background='white')
    lab1=Label(Repo,text="Reportes", font=("Cambria", 33), bg="#063970", fg="white", width="550", height="2")
    lab1.pack()

ventana = tk.Tk()
ventana.title('Reconocimiento Facial')
ventana.geometry('650x558+320+0')
ventana.resizable(False,False)
ventana.configure(background='white')
main_title=Label(text="Inicio de Sesión", font=("Cambria", 33), bg="#063970", fg="white", width="550", height="2")
main_title.pack()
color = '#063970'
#ventana['bg'] = color
imagen=Image.open('loo.jpg')
imagen= imagen.resize((280,200), Image.ANTIALIAS)
photoImg=ImageTk.PhotoImage(imagen)
panel=tk.Label(ventana, image=photoImg).pack()

user=Label(text="Nombre", bg="white",font=('Time New Roman', 15))
user.place(x=280, y=330)
passw=Label(text="Contraseña",bg="white", font=('Time New Roman', 15))
passw.place(x=270, y=390)
user=StringVar()
passw=StringVar()
caja1 = Entry(textvariable=user, width="45",border="1",highlightthickness=1)
caja1.config(highlightbackground=color, highlightcolor=color)
caja2 = Entry(textvariable=passw, width="45", show="*",highlightthickness=1)
caja2.config(highlightbackground=color, highlightcolor=color)
caja1.place(x=200, y =360)
caja2.place(x=200, y=420)

btn=Button(ventana,text='Entrar', command=login, width="14", height="2",fg="white", bg='#1e81b0',font=('Arial Rounded MT Bold', 12))
btn.place(x=200, y=450)
boton1 = Button(ventana,text='Registro', bg="#1e81b0",command=controlusuarios,width="14", fg="white",height="2", font=('Arial Rounded MT Bold', 12))
boton1.place(x=341, y=450)



ventana.mainloop()

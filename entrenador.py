# entrenador con EigenFaces
import sqlite3
import cv2
import os
import numpy as np 
from PIL import Image
import xml.etree.ElementTree
db = sqlite3.connect('C:/Users/MARIELA\Videos/proyecto/admin.db')
c = db.cursor()
dataPath = 'C:/Users/MARIELA/Videos/proyecto/data'
peopleList = os.listdir(dataPath)
print('Lista de personas: ', peopleList)
 # 
labels = []
facesData = []
label = 0

for nameDir in peopleList:
    personPath = dataPath + '/' + nameDir
    print( 'Leyendo las imagenes' )

    for fileName in os.listdir(personPath):
        print('Rostros: ', nameDir + '/' + fileName)
        labels.append(label)
        facesData.append(cv2.imread(personPath+'/'+fileName,0))
        image = cv2.imread(personPath +'/'+ fileName,0)
        cv2.imshow('image',image)
        cv2.waitKey(10)
# Metodos para entrenar el reconocedor
#face_recognizer = cv2.face.createEigenFaceRecognizer()
#face_recognizer = cv2.face.createFisherFaceRecognizer()
#face_recognizer = cv2.face.createLBPHFaceRecognizer()
face_recognizer= cv2.face.createEigenFaceRecognizer() 
# Entrenando el reconcedor de rostros
print("Entrenando..")
face_recognizer.train(facesData, np.array(labels))
# Almancenand el modelo obtenido 

face_recognizer.save('/home/pi/reconocimientofacial/modelEingenFace.xml')
print("Modelo almacenado..")


cv2.destroyAllWindows()
        

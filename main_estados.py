
from timeit import default_timer as timer

from libgeometrica import *
from graficador import *
#from analisis import *
from ximbi3 import *
import time
import config1



def imagen(equis1, ygriega1):
	#cv2.destroyAllWindows()
	start = timer()
	#se setean los puntos

	#img = cv2.imread('5.jpeg')
	#
	#cap = cv2.VideoCapture(0)
	cap = cv2.VideoCapture('/home/cactus/Documents/1_AOB/DSRLLO/Uniendo0/Estados0/0.7.5/MAH01277vR.mov')
	# Read until video is completed
	while(cap.isOpened()):
		# Capture frame-by-frame

		ret, frame = cap.read()
		if ret == True:
			pointsInside,res = contornos(frame)
			#se ordena el arreglo de menor a mayor por la coordenada x.
			pointsInside.sort()
			#pointsInside = [(10, 20), (100, 80), (230, 106), (260, 230), (320, 310), (350, 360), (512,512)]
			#se setea el color de los puntos
			colorPuntos = [0, 0, 255]
			#se setea el color de las lineas
			colorLinea = [0, 0, 255]
			#se setea el grosor de la linea y los puntos
			thickness = 3
			##################Punto referencia#############
			equis = equis1
			ygriega = ygriega1
		##############################################
		#se definen los valores min y max de el rango permitido
			xmax = 500
			ymax = 500
			xmin = 0
			ymin = 0
		#se define el valor de busqueda de siguiente nodo (fin de hilera)
			valordebusqueda = 300
			interseccion = []
		#se agregan los valores permitidos a pointsInside2
			#time.sleep(1)
			#se define el valor de busqueda de siguiente nodo (fin de hilera)
			#valordebusqueda = 300
			#interseccion = []
		#se agregan los valores permitidos a pointsInside2
			#interseccion,sentido,img = graficar(res,pointsInside,xmax,ymax,xmin,ymin,colorPuntos,colorLinea,thickness,equis,ygriega,valordebusqueda)	
			diferencia,interseccion,sentido,distanciaprevio,distanciasiguiente,img = graficar(res, pointsInside,xmax,ymax,xmin,ymin,colorPuntos,colorLinea,thickness,equis,ygriega,valordebusqueda)
			#return diferencia,distanciaprevio,distanciasiguiente
			cv2.imshow('Frame',frame)
			cv2.imshow('Frame2',img)
			#return diferencia,distanciaprevio,distanciasiguiente
			config1.diferencia=diferencia
			config1.distanciaprevio=distanciaprevio
			config1.distanciasiguiente=distanciasiguiente
			print("paso siguiente")
			print(distanciasiguiente)
			print("paso siguiente")
			print(config1.distanciasiguiente)
			print("equis e igriega")
			print(equis1, ygriega1)
			


			# Press Q on keyboard to  exit
			if cv2.waitKey(25) & 0xFF == ord('q'):
				break

		# Break the loop
		else: 
			break

	# When everything done, release the video capture object
	cap.release()

	# Closes all the frames
	cv2.destroyAllWindows()


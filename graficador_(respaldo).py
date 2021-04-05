import numpy as np
import cv2
#import matplotlib.pyplot as plt
from libgeometrica import *
import pdb


class Point: 
	def __init__(self, x, y): 
		self.x = x 
		self.y = y 

def graficar(img, pointsInside,xmax,ymax,xmin,ymin,colorPuntos,colorLinea,thickness,equis,ygriega,valordebusqueda):
	#img = np.zeros([512, 512, 3],np.uint8)
	#print("pointsinside ==================", pointsInside)
	pointsInside2 = []
	length = len(pointsInside)
	#print("len(pointsInside) =", len(pointsInside))





###############################################################
# 0. ######## No hay plantas en el rango de vision ############
###############################################################
	if length == 0:
		print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1!!!!!!!!!!!!!!!!!!!!!!!!!!!')
		cv2.line(img, (xmin,int(ymax/2)),(xmax,int(ymax/2)), colorLinea, thickness)
		
		if ygriega < ymax/2: #estamos sobre la linea virtual creada para este caso
			p1 =  Point(xmin, int(ymax/2))
			q1 =  Point(xmax, int(ymax/2))
			p2 =  Point(equis, ygriega) 
			q2 =  Point(equis,ymax)
			print("p1 = {},q1 = {},p2 = {},q2 = {}".format(p1,q1,p2,q2))

			if doIntersect(p1, q1, p2, q2): ###Redundante para este caso
				interseccion = line_intersection(((xmin,int(ymax/2)),(xmax,int(ymax/2))), ((equis, ygriega), (equis,ymax)))
				
				print("interseccion[0]", interseccion[0])
				
				a = np.float32(interseccion[0])
				b = np.float32(interseccion[1])
				cv2.circle(img, (a,b), 10, [0, 255, 100], thickness)

###############################################################
###############################################################



	for i in range(length): 
		#print("lo hace o no lo hace????? a ? =")
		#if i == len(pointsInside) :
		#	break
		print("WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWw")
#####Verifica qeu los puntos esten dentro del rango de vision, y si es asi, los agrega a pointsinside2

		if pointsInside[i][0] <= xmax and pointsInside[i][0] >= xmin and pointsInside[i][1] <= ymax and pointsInside[i][1] >= ymin:
			#pointsInside[i] = ("x","x")
			pointsInside2.append(pointsInside[i])
			
			print("pointsinside2",pointsInside2)
			#print("pointsinside",i,pointsInside[i])
	#se dibuja el primer circulo
	#cv2.circle(img, pointsInside2[0], 10, colorPuntos, thickness) 
	#se dibujan los puntos siguientes
	for index, item in enumerate(pointsInside2):
		print("WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWw")

		if index == len(pointsInside2) -1:
			print("aca 1")
			break
		cv2.circle(img, pointsInside2[index + 1], 10, colorPuntos, thickness) 
		cv2.line(img, item, pointsInside2[index + 1], colorLinea, thickness)
	starpoint = (equis,ygriega)
	endpoint = (equis,ymax) #se arregló esto
	endpoint2 = (equis,ymin)
	interseccion = []
	sentido=0
	distanciaprevio=0
	distanciasiguiente=	0

	
	for index, item in enumerate(pointsInside2): 
		print("WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWw")
		#print("index = {}, item = {}, len(pointsinside2) - 1 = {}".format(index,item,(len(pointsInside2)-1)))
		if index == len(pointsInside2) -1:
			print("aca 2")
			###### se esta recorriendo el último centro de planta ######
			break

		# Driver program to test above functions: 
		# print(item)
		p1 = Point(item[0],item[1]) 
		q1 = Point(pointsInside2[index + 1][0], pointsInside2[index + 1][1]) 
		p2 = Point(starpoint[0], starpoint[1]) 
		q2 = Point(endpoint[0],endpoint[1])
		q3 = Point(endpoint2[0],endpoint2[1])
		largo = len(pointsInside2) - 1
		#if equis > pointsInside2[largo][0]:
		#	print("se llegó al final de la hilera")
		#	break
		
	  
		if doIntersect(p1, q1, p2, q2):
			cv2.line(img, starpoint, endpoint, colorLinea, thickness) 
			print("entrando en el primer if.............")
			##################################################################################
			colorLineatemp = [255, 40, 100]
			cv2.line(img, (starpoint[0],pointsInside2[index][1]), pointsInside2[index], colorLineatemp, thickness)
			cv2.line(img, (starpoint[0],pointsInside2[index+1][1]), pointsInside2[index + 1], colorLineatemp, thickness)
			print("punto previo x:",pointsInside2[index][0])
			print("starpoint:",starpoint[0])
			print("punto siguiente x:",pointsInside2[index + 1][0])
			distanciaprevio =  lineMagnitude(starpoint[0],pointsInside2[index][1], pointsInside2[index][0],pointsInside2[index][1])
			distanciasiguiente = lineMagnitude(starpoint[0],pointsInside2[index+1][1], pointsInside2[index + 1][0],pointsInside2[index + 1][1])
			
			#print("distanciaprevio:",distanciaprevio)
			#print("distanciaprevio:",distanciasiguiente)
			####################################################################################
			sentido=1

			
			print("cositossssssssss")
			#print("LLamada a graficador con startṕoint {}, endpoint{}, item{}".format(starpoint,endpoint,item))
			
			interseccion = line_intersection((starpoint, endpoint), (item, pointsInside2[index + 1]))
			a = np.float32(interseccion[0])
			b = np.float32(interseccion[1])
			cv2.circle(img, (a,b), 10, [0, 255, 100], thickness)
			print("interseccion", interseccion)
			#print("Yes")
			
			#sprint(pointsInside2[largo][0])
			#se crea un if para detectar si se llego al final de la hilera
			
			#if lineMagnitude(a,b,pointsInside2[largo][0],pointsInside2[largo][1]) < valordebusqueda:

			#	print("se llegó al final de la hilera")
			#	break


		if doIntersect(p1, q1, p2, q3):
			cv2.line(img, starpoint, endpoint2, colorLinea, thickness)
			##################################################################################
			print("entrando en el segundo if.............")
			colorLineatemp = [255, 40, 100]
			cv2.line(img, (starpoint[0],pointsInside2[index][1]), pointsInside2[index], colorLineatemp, thickness)
			cv2.line(img, (starpoint[0],pointsInside2[index+1][1]), pointsInside2[index + 1], colorLineatemp, thickness)
			print("punto previo x:",pointsInside2[index][0])
			print("starpoint:",starpoint[0])
			print("punto siguiente x:",pointsInside2[index + 1][0])
			distanciaprevio =  lineMagnitude(starpoint[0],pointsInside2[index][1], pointsInside2[index][0],pointsInside2[index][1])
			distanciasiguiente = lineMagnitude(starpoint[0],pointsInside2[index+1][1], pointsInside2[index + 1][0],pointsInside2[index + 1][1])
			
			#print("distanciaprevio:",distanciaprevio)
			#print("distanciaprevio:",distanciasiguiente)
			####################################################################################
			sentido=-1

			#pdb.set_trace()
			print("cositossssssssss_2")
   


			interseccion = line_intersection((starpoint, endpoint2), (item, pointsInside2[index + 1]))
			print("interseccion", interseccion)

			a = np.float32(interseccion[0])
			b = np.float32(interseccion[1])
			cv2.circle(img, (a,b), 10, [0, 255, 100], thickness)
			#print("Yes")
			
			#sprint(pointsInside2[largo][0])
			#se crea un if para detectar si se llego al final de la hilera
		


			#if lineMagnitude(a,b,pointsInside2[largo][0],pointsInside2[largo][1]) < valordebusqueda:
			#	print("se llegó al final de la hilera")
			#	break
		
		if not(doIntersect(p1, q1, p2, q2 )) and not(doIntersect(p1, q1, p2, q3)):
		#si no intersecta con la linea virtual:
			print("no hay intersección")
			print("puntos:", pointsInside2)
			
			pass
		#else:
		#	return None 
	#se dibuja el punto de referencia
	cv2.rectangle(img,(xmin,ymin),(xmax,ymax),(0,0,255),3)
	cv2.circle(img, starpoint, 10, [0, 255, 0], thickness)
	#cv2.imshow('Navegacion',img) 
	#print("Aqui grafica!!!!!!!!!!!!!!!!!!!")
	#cv2.waitKey(0)
	#plt.imshow(img)
	#plt.ion()
	#plt.pause(0.01)
	#plt.show()
	print("equis",equis)
	print("ygriega",ygriega)
	print("interseccion[0]",interseccion[0])
	print("interseccion[1]",interseccion[1])
	#diferencia=lineMagnitude(equis,ygriega,interseccion[0],interseccion[1])
	diferencia=0
	#print("ladiferencia")
	#print(diferencia)
	return diferencia,interseccion,sentido,distanciaprevio,distanciasiguiente,img
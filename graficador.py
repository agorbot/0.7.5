import numpy as np
import cv2
#import matplotlib.pyplot as plt
from libgeometrica import *
import pdb
import time


class Point: 
	def __init__(self, x, y): 
		self.x = x 
		self.y = y 

def graficar(img, pointsInside,xmax,ymax,xmin,ymin,colorPuntos,colorLinea,thickness,equis,ygriega,valordebusqueda):
	#img = np.zeros([512, 512, 3],np.uint8)
	#print("pointsinside ==================", pointsInside)
	pointsInside2 = []
	length = len(pointsInside)
	#print("length = ", length)
	#print("len(pointsInside) =", len(pointsInside))



	starpoint = (equis,ygriega) # punto referencia
	endpoint = (equis,ymax) #se arregló esto
	endpoint2 = (equis,ymin)
	interseccion = []
	sentido=0
	distanciaprevio=0
	distanciasiguiente=	0

###############################################################
# 0. ######## No hay plantas en el rango de vision ############
###############################################################
	if length == 0:
		print("Caso en el que no hay ninguna planta")
		cv2.line(img, (xmin,int(ymax/2)),(xmax,int(ymax/2)), colorLinea, thickness)
		#starpoint = (equis,ygriega)

		###############################################################
		############### Referencia sobre linea virtual ################
		###############################################################

		
		p1 =  Point(xmin, int(ymax/2))
		q1 =  Point(xmax, int(ymax/2))
		p2 =  Point(equis, ymin) 
		q2 =  Point(equis,ymax)
		#print("p1 = {},q1 = {},p2 = {},q2 = {}".format(p1,q1,p2,q2))

		if doIntersect(p1, q1, p2, q2): ###Redundante para este caso
			interseccion = line_intersection(((xmin,int(ymax/2)),(xmax,int(ymax/2))), ((equis, ygriega), (equis,ymax)))
				
			#print("interseccion[0]", interseccion[0])
				
			a = np.float32(interseccion[0])
			b = np.float32(interseccion[1])
			cv2.circle(img, (a,b), 10, [0, 255, 100], thickness)
			cv2.line(img,starpoint,(a,b), colorLinea, thickness) # Linea vertical

		###############################################################
		############### Referencia bajo linea virtual #################
		###############################################################

		if ygriega > ymax/2: #estamos bajo la linea virtual creada para este caso
			print("bajo la linea")
			sentido= -1
		if ygriega < ymax/2: #estamos sobre la linea virtual creada para este caso, ya que las y van hacia abajo
			print("sobre la linea")
			sentido= 1	
###############################################################
###############################################################

###############################################################
# 1. ######## Hay una planta en el rango de vision ############
###############################################################
	if length == 1:
		print("Caso en el que hay una planta")

		#print("Lo basico.....----->o0<-----")
		#print("pointsInside",pointsInside)
		cv2.line(img, (xmin,pointsInside[0][1]),(xmax,pointsInside[0][1]), colorLinea, thickness) # Dibuja linea desde el centro de 
		#la planta a los extremos de vision.

		#time.sleep(3)
		#interseccion = (0,0)

		###############################################################
		############### Referencia sobre linea virtual ################
		###############################################################

		
		p1 =  Point(xmin, int(pointsInside[0][1]))
		q1 =  Point(xmax, int(pointsInside[0][1]))
		p2 =  Point(equis, ymin) 
		q2 =  Point(equis,ymax)
		#print("p1 = {},q1 = {},p2 = {},q2 = {}".format(p1,q1,p2,q2))

		if doIntersect(p1, q1, p2, q2): ###Redundante para este caso
			interseccion = line_intersection( ((xmin,int(pointsInside[0][1])),(xmax,int(pointsInside[0][1]))), ((equis, ygriega), (equis,ymax)))
				
			#print("interseccion[0]", interseccion[0])
				
			a = np.float32(interseccion[0])
			b = np.float32(interseccion[1])
			cv2.circle(img, (a,b), 10, [0, 255, 100], thickness)
			cv2.line(img,starpoint,(a,b), colorLinea, thickness) # Linea vertical


		if ygriega > pointsInside[0][1]/2: #estamos bajo la linea virtual creada para este caso, ya que las y van hacia abajo
			print("bajo la linea")
			sentido= -1
		if ygriega < pointsInside[0][1]/2: #estamos sobre la linea virtual creada para este caso, ya que las y van hacia abajo	
			print("sobre la linea")
			sentido= 1




###############################################################
###############################################################

###############################################################
###############################################################
###############################################################
# 2. ##### Hay mas de una planta en el rango de vision ########
###############################################################
###############################################################
###############################################################

	if length >1:
		print("Caso en el que hay más de una planta")

		for i in range(length): 
			#print("I = ", i)
			#print("lo hace o no lo hace????? a ? =")
			#if i == len(pointsInside) :
			#	break
			
	#####Verifica qeu los puntos esten dentro del rango de vision, y si es asi, los agrega a pointsinside2

			if pointsInside[i][0] <= xmax and pointsInside[i][0] >= xmin and pointsInside[i][1] <= ymax and pointsInside[i][1] >= ymin:
				#pointsInside[i] = ("x","x")
				pointsInside2.append(pointsInside[i])
			
				#print("pointsinside2",pointsInside2)
				#print("pointsinside",i,pointsInside[i])
		#se dibuja el primer circulo
		#cv2.circle(img, pointsInside2[0], 10, colorPuntos, thickness) 
		#se dibujan los puntos siguientes

##############################################################################################
##############################################################################################

		
##############################################################################################
##############################################################################################
		##############Dibuja circulos en los centros y lineas entre estos para seguir  #######

		for index, item in enumerate(pointsInside2):
			################################################################################
			#### Linea desde inicio de vision a primer centro ##############################
			################################################################################
			if index == 0:
				cv2.line(img, item, (xmin,pointsInside2[index][1]), colorLinea, thickness)

			################################################################################
			#### Linea desde ultimo centro a fin de vision #################################
			################################################################################
			if index == len(pointsInside2) -1:
				#print("aca 1")
				cv2.line(img, item, (xmax,pointsInside2[index][1]), colorLinea, thickness)
				break

			################################################################################
			############ Linea entre las plantas  ##########################################
			################################################################################	
			cv2.circle(img, pointsInside2[index +1], 10, colorPuntos, thickness) 
			cv2.line(img, item, pointsInside2[index + 1], colorLinea, thickness)
			
##############################################################################################
##############################################################################################



		##############################################################################################
		##############################################################################################
		##############################################################################################
		##############################################################################################
		##############################################################################################


		#print("tipo pointsinside",type(pointsInside2))

		punto_nuevo=(starpoint[0],-1) # punto para referencia y pointsInside3!!!
		pointsInside3=pointsInside2
		pointsInside3.append(punto_nuevo)
		#print("pointsinside3",pointsInside3)
		pointsInside3.sort()
		#print("pointsinside3 ordenado =",pointsInside3)

		

		#print("starpoint_np",starpoint_np)


		for index, item in enumerate(pointsInside3): 

			if item[1]== -1:
				#print("Index aca =", index)

				
				if index == 0:
					print("primer_subcaso")
####*************************************************************************####
####*************************************************************************####

########### Punto de referencia sobre la linea ###########################
					

						
					p1 = Point(xmin,pointsInside3[1][1]) 
					q1 = Point(pointsInside3[1][0], pointsInside3[1][1]) 
					p2 = Point(starpoint[0], ymin) 
					q2 = Point(endpoint[0],ymax)
					#q3 = Point(endpoint2[0],endpoint2[1])
					#print("p1 = {} {}, q1 = {} {}, p2 = {} {}, q2 = {} {}".format(p1.x,p1.y,q1.x,q1.y,p2.x,p2.y,q2.x,q2.y))

					if doIntersect(p1, q1, p2, q2): 
						
							
						interseccion = line_intersection(((p1.x,p1.y),(q1.x,q1.y)), ((p2.x,p2.y), (q2.x,q2.y)))

						a = np.float32(interseccion[0])
						b = np.float32(interseccion[1])
						cv2.circle(img, (a,b), 10, [0, 255, 100], thickness)
						cv2.line(img,starpoint,(a,b), colorLinea, thickness) # Linea vertical
					
						#print("interseccion", interseccion)
						break		

########### Punto de referencia bajo la linea ###########################
					if ygriega < pointsInside3[1][1]:
						print("encima de la linea")
						sentido= 1
					else:
						print("bajo la linea")
						sentido= -1



						break
####*************************************************************************####
####*************************************************************************####				
							    
				if (index == (len(pointsInside3) - 1)): #or (equis==pointsInside3[len(pointsInside3) - 1][0]):							
					print("tercer_subcaso")

########### Punto de referencia sobre la linea ###########################
					
					
						

					#if (equis==pointsInside3[len(pointsInside3) - 1][0]):
					#	print("caso singular********************************************************************")

						#break
					p1 = Point(pointsInside3[len(pointsInside3)-2][0],pointsInside3[len(pointsInside3)-2][1]) 
					q1 = Point(xmax, pointsInside3[len(pointsInside3)-2][1]) 
					p2 = Point(starpoint[0], ymin) 
					q2 = Point(endpoint[0],ymax)
					#q3 = Point(endpoint2[0],endpoint2[1])
					#print("p1 = {} {}, q1 = {} {}, p2 = {} {}, q2 = {} {}".format(p1.x,p1.y,q1.x,q1.y,p2.x,p2.y,q2.x,q2.y))

					if doIntersect(p1, q1, p2, q2): 
						
							
						interseccion = line_intersection(((p1.x,p1.y),(q1.x,q1.y)), ((p2.x,p2.y), (q2.x,q2.y)))
						a = np.float32(interseccion[0])
						b = np.float32(interseccion[1])
						cv2.circle(img, (a,b), 10, [0, 255, 100], thickness)
						cv2.line(img,starpoint,(a,b), colorLinea, thickness) # Linea vertical
					
						#print("interseccion", interseccion)
						break

########### Punto de referencia bajo la linea ###########################
					if ygriega < pointsInside3[len(pointsInside3)-2][1]: #sobre la linea -2 por que sino toma el valor del -1
						print("encima de la linea")
						sentido= 1
					if ygriega > pointsInside3[len(pointsInside3)-2][1]: #bajo la linea -2 por que sino toma el valor del -1
						print("abajo de la linea")
						sentido= -1
						break	
####*************************************************************************####
####*************************************************************************####
				else:

					print("segundo_subcaso")
					#print("index =", index)
					#print(len(pointsInside3))
					
					
			#### primero checkear si se esta sobre o bajo la linea #####
					#print("pointsInside3[index-1]", pointsInside3[index-1])

					p1 = Point(pointsInside3[index-1][0],pointsInside3[index-1][1]) 
					q1 = Point(pointsInside3[index+1][0],pointsInside3[index+1][1]) 
					p2 = Point(starpoint[0], ymin) 
					q2 = Point(starpoint[0], ymax)
					#q3 = Point(endpoint2[0],endpoint2[1])
					#print("p1 = {} {}, q1 = {} {}, p2 = {} {}, q2 = {} {}".format(p1.x,p1.y,q1.x,q1.y,p2.x,p2.y,q2.x,q2.y))

					if doIntersect(p1, q1, p2, q2): 
													
						interseccion = line_intersection(((p1.x,p1.y),(q1.x,q1.y)), ((p2.x,p2.y), (q2.x,q2.y)))

						a = np.float32(interseccion[0])
						b = np.float32(interseccion[1])
						cv2.circle(img, (a,b), 10, [0, 255, 100], thickness)
						cv2.line(img,starpoint,(a,b), colorLinea, thickness) # Linea vertical
					
						#print("interseccion", interseccion)
						#print("ygriega =", ygriega)
 ###### dependiendo de si esta sobre o bajo la linea, obtener la distancia desde el punto de referencia a la linea virtual #######

					if (interseccion[1]>ygriega): # Se esta sobre la linea 
						print(" Se esta sobre la linea !!!! ")	
						sentido = 1			
					if (interseccion[1]<ygriega): # Se esta bajo la linea
						print(" Se esta bajo la linea !!!! ")
						sentido = -1

						break




	#######################   ver si se esta sobre o bajo la linea ##########
					###***** ¡¡¡¡¡Aca quedamos!!!!! *******######




	########### Punto de referencia sobre la linea ########################### 



					#break



			#print("index = {}, item = {}, len(pointsinside2) - 1 = {}".format(index,item,(len(pointsInside2)-1)))			
####*************************************************************************####
####*************************************************************************####
	#print("interseccion =", interseccion)
	diferencia = abs(ygriega - interseccion[1]) 
	distanciaprevio=0
	distanciasiguiente=0
	print("diferencia = {},interseccion = {}, sentido = {}, distanciaprevio= {}, distanciasiguiente= {}".format(diferencia,interseccion, sentido,distanciaprevio,distanciasiguiente))

			#if starpoint[0] > item[0]:
				# Debe seguir el for, hasta encontrar el punto que sea mayor. Cuando quede menor, encontrar los puntos previo 
				#y siguiente, para luego  
			#	print("el punto de referencia en x {}, es mayor que el punto {}, en {} ".format(starpoint[0],index,item[0]))
				#break
			#else:
				# Hay que distinguir entre 3 casos:
				#	- el index del punto siguiente es = 0 => estamos antes de la  primera planta.
				#	- el index del punto siguiente es != 0 y = a [len(pointsInside2) -1] => estamos despues 

				#if starpoint[0]< index 
			#	print("animate")

	return(diferencia,interseccion, sentido,distanciaprevio,distanciasiguiente,img)

			#print("index = {}, item = {}, len(pointsinside2) - 1 = {}".format(index,item,(len(pointsInside2)-1)))
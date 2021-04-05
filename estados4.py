from random import randint
import time 
from main_estados import imagen  
import cv2
import serial
from threading import Thread
import threading
import config1




##======================================
#uno = serial.Serial('com3',9600,timeout=None)         # para Windi
#uno = serial.Serial('/dev/ttyACM0',9600,timeout=None)  # Para Linex
uno = serial.Serial('/dev/ttyUSB0',9600,timeout=None)  # Para Linex
time.sleep(2)


########################################################
##########  Maquina de estados finita  #################
########################################################
########################################################


########################################################
#############  Generar señal de muestreo ###############
########################################################



########################################################
########################################################


#########################################################
################ Variables globales #####################
#########################################################
x=0
y=0

is_done = False


################################################
#- hilo 1 llama a Analisis, ximbi, etc... 
#- Entrega valor de Distancia (1°)
#- Entrega otros valores
################################################

########################################################
############### hilo1 ##################################
########################################################
def ImagenThread():
    global is_done
    Distancia = 0
    hilo_actual = threading.current_thread().getName()
    print('Hilo actual', hilo_actual)
    
    ###############################
    imagen(260,300)

    #for t in range(11):
    #    print("t =",t)
        #if t == 10:
    #    Distancia=Distancia+1
    #    print("Distancia =", Distancia)
    #    config1.variable1=Distancia
    #    evento.set()
    #    print("Evento set", evento.is_set())
        #evento.wait()
    ###############################  



    time.sleep(0.00000001)  
        #print('Hola--->o0<---')
    is_done = True
    evento.set()
########################################################
########################################################



###############################################
#hilo2, toma la variable desde config, la 
#codifica y envía al micro
###############################################



########################################################
############### hilo2 ##################################
########################################################
def ThreadLeerVariable():
    while not is_done:
      print("evento is_done en 2", is_done)
      print("evento set en 2", evento.is_set())
      #########################################
      # - Llamar a codificador
      # - Enviar a micro
      #########################################
      evento.clear()
      print("Funcion 2 ")
      #print('config1.variable1 en thread 2 =', config1.variable1)
      print("la diferencia es:",config1.diferencia)
      evento.wait()
########################################################
########################################################







########################################################
########################################################
def Analisis():
	x=200
	y=600
	print("en estado analisis")
	#diferencia,distanciaprevio,distanciasiguiente = imagen(x,y)
	thread1 = ImagenThread()
	thread1.start()
	threads.append(thread1)
	#imagen(x,y)
	print("paso imagen")
	print(config.diferencia)
	print(config.distanciaprevio)
	print(config.distanciasiguiente)
	diferencia=30
	distanciaprevio=40
	distanciasiguiente=50
	valor1=10
	valor2=100
	valor3=100
	#if (diferencia>valor1):
	#	print("accionar")
	#	Comunicacion(diferencia)
	#if (distanciaprevio>valor2):
	#	print("accionar2")
	#	Comunicacion(distanciaprevio)
	#if (distanciasiguiente>valor3):
	#	print("accionar3")
	#	Comunicacion(distanciasiguiente)
########################################################
########################################################
	
	
	
########################################################
########################################################
##================================================
##========= Estado comunicacion con Micro ========
##================================================
########################################################
########################################################
def Comunicacion(distancia):
    n=distancia
    tres = str(n)
    inicio = "<"
    fin = ">"
    mensaje = inicio + tres + fin
    mensaje_byte = mensaje.encode('ascii')
    print (mensaje_byte)
    print("mensaje--- = ",type(mensaje_byte))
    led_off(mensaje_byte)
########################################################
########################################################

########################################################
########################################################
############== Envio a micro ==#########################
########################################################
########################################################
def Crear_mensaje(data):

	n=data
	n=round(n,0)  # Se aproxima a un entero 
	n=int(n)      # Se trunca
	tres = str(n)
	inicio = "<"
	fin = ">"
	mensaje = inicio + tres + fin
	mensaje_byte = mensaje.encode('ascii')
	print (mensaje_byte)
	#print("mensaje--- = ",type(mensaje_byte))

	return(mensaje_byte)
########################################################
########################################################


########################################################
########################################################
def led_off(datos):

	print("hola off")
	print("datos", datos)
	uno.write(datos) # Escribir
	
	print("enviado=============")
	time.sleep(2)
	#uno.close()
	#time.sleep(2)
	print("ahora si quedo libre")
	llegada = uno.read(6)
	print(llegada[0]) 
	print(llegada[1])
	print(llegada[2])
	print(llegada[3])
	print(llegada[4])
	print(llegada[5])

	if llegada[0] == 60:
		print("El valor es igual a = <")
		valor = ((llegada[2]-48)*100)+((llegada[3]-48)*10)+(llegada[4]-48)
		if (llegada[1]==45):
			valor=valor*(-1)
		print(valor)
		print("llegada = >")

########################################################
########################################################




########################################################
########################################################
class WorkerThread(Thread):
    def run(self):
        print("started")
        while True:            
            ret, frame = cap.read()
            cv2.imshow('Face', frame)
            k = cv2.waitKey(5) & 0xFF
            if k == ord('q'):
                break
########################################################
########################################################




evento = threading.Event()
#listo
#bloquea = threading.Lock()
hilo1 = threading.Thread(target=ImagenThread)
hilo2 = threading.Thread(target=ThreadLeerVariable)
hilo1.start()
hilo2.start()
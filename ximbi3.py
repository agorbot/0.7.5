# -*- coding: utf-8 -*-
# Load the opencv library and drawing tools
# ------------------------------------------------------
import cv2
#import matplotlib.pyplot
import numpy as np
from PIL import Image
import math

def contornos(frame):
    pointsInside = []

   ##===================cambio de dimenciones===============    
    height , width , layers =  frame.shape
        
    new_h=500
    new_w=500
    frame = cv2.resize(frame, (new_w, new_h)) 
##=======================================================
##==============Primera capa=============================

    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    blurred=cv2.blur(frame, (4,4),0.001) 
    kernel = np.ones((1,1),np.uint8)
    erosion = cv2.erode(blurred,kernel,iterations = 5)
##=======================================================
    h=frame_hsv[:,:,0]
        
    b=erosion[:,:,0]
    g=erosion[:,:,1]
    r=erosion[:,:,2]

    #############################################################
    sumaton=0.000000001
        
    exg =  2 * g - r - b
        
    exr = 1.4*r-g

    ex_comb=exg-exr

    veg = g / ((r ** 0.667) * (b ** (1 - 0.667))+sumaton)
    cive = 0.441 * r - 0.811 * g + 0.385 * b + 18.75
       
##=================================================================
##=================================================================
       

    exg2=exg*1 - 18

    exg3=exg2+exr
    ex_comb2=ex_comb -18

    veg2=veg*0.5 
        
#===================Juntando indices =============

##=================Binarizando====================

    ret,thresh1 = cv2.threshold(exr,0,255,cv2.THRESH_BINARY)
    ret,thresh2 = cv2.threshold(cive,0,255,cv2.THRESH_BINARY)
        
    ret2,otsux = cv2.threshold(exg2,0,255,cv2.THRESH_OTSU)
    otsux_n = cv2.bitwise_not(otsux)
        

    print("numero = ", type(otsux[0,1]))
    print("ximiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii")

    otsux_n = cv2.cvtColor(otsux_n, cv2.COLOR_GRAY2RGB)
        
    outputx2_3= cv2.bitwise_and(otsux_n, frame)
        
    #cive_n=cv2.bitwise_not(cive)
    #exr_n=cv2.bitwise_not(exr)
##===============================================================
##====================Juntando con or===========================

    sal_1=cv2.bitwise_and(thresh1,thresh2)
        
        
   
    sal_1int = sal_1.astype(int)
        
        
    otsux = otsux.astype(float)
      
       
    sal_2 = cv2.bitwise_and(sal_1,otsux)
        
    sal_2_8 = cv2.convertScaleAbs(sal_2)


    sal_2_not = cv2.bitwise_not(sal_2_8)
        
    sal_2_out = cv2.cvtColor(sal_2_not, cv2.COLOR_GRAY2RGB)
    salida_total_1= cv2.bitwise_and(sal_2_out, frame)

    cv2.imshow('sal_2',sal_2)
        
    cv2.imshow('sal_2_not',sal_2_not)
    cv2.imshow('salida_total_1',salida_total_1)
    #writer.write(salida_total_1)

##==========================================================

##==================================================== 



    #cv2.rectangle(frame,(20,20),(30,30),(0,255,0),2)

##================Mostrar imagenes===============
    #nootsux=cv2.bitwise_not(otsux)
    #contours_2, _ = cv2.findContours(otsux, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)     # para Linex
    contours_2, _ = cv2.findContours(sal_2_not, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)     # para Wendy
    print("hola")
    for contour_2 in contours_2:
        area = cv2.contourArea(contour_2)
        #print ('area =', area)
        if area > 200:  # Definicion para eleccion de imagen
            M = cv2.moments(contour_2)
            cx = int((M['m10']/M['m00']))
            cy = int((M['m01']/M['m00']))
            x,y,w,h = cv2.boundingRect(contour_2)
            cv2.rectangle(salida_total_1,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.circle(salida_total_1,(cx, cy), 5, (0,0,255), -1)
            #print("centro =", cx, cy)
            pointsInside.append((cx,cy))



    
    #cv2.imshow("salida_frame",frame)
    #cv2.imshow("otsux_2",otsux_2)
    #cv2.imshow("erosion",erosion)    
    #cv2.imshow("salida_erosion",outputx)
    #cv2.imshow("outputx_2",outputx_2)
        
    #cv2.imshow("th3",th3)
    #cv2.imshow("exg",blurred)
    #cv2.imshow("mexg",mexg)
#    cv2.imshow("images",outputx)
    print("pointsinside", pointsInside)
    print("paso!!!!")
##===============================================
    return(pointsInside,salida_total_1)
    #cv2.imshow("imagesframe",frame)
    #if cv2.waitKey(1) & 0xFF == ord('q'):
    #    break
#cap.release()
#cv2.destroyAllWindows()
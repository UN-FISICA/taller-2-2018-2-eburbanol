# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 49:03:10 2018

@author: Eduardo Burbano

Punto 2
"""
from turtle import *


def cuad(lado):
    
   

    for i in range (4):
        for i in range(1):
            penup()  
            forward(10)
            right(90)            
            forward(10)
            right(90)
        n=input("Ingrese el numero de lados del poligono. Minimo 3 ")
        n=int(n)    
            for i in range (n):             
                pendown()
                forward(20)
                right(360/n)
                penup()
            
            forward(10)
            right(90)
            forward(10)
        pendown() 
        forward(110)
        right(90)
cuad(4)


    
            
done()

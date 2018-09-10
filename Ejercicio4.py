# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 12:07:18 2018

@author: Eduardo Burbano

Punto 4.
"""
from math import *
from turtle import *

a=input("Ingrese el numero de lados del poligono. Minimo 3 ")
a=int(a)
b=input("Ingrese el numero de filas de la piramide ")
b=int(b)

def poli(n):
    for i in range(n):
        forward(2*25*sin(pi/n))
        left(360/n)
        
def fila(lados,filas):
    for i in range(filas):
        poli(lados)
        penup()
        forward(50)
        pendown()   
    
def piramide(lados,filas):
    for i in range(filas,0,-1):
        fila(lados,i) 
        penup()
        backward((i*50))
        forward(50/2)
        left(90)
        forward(30+20)
        right(90)
        pendown()
    done()

penup()
goto(-130,-130)
pendown()
        
piramide(a,b)

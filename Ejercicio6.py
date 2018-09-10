# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 14:22:12 2018

@author: Eduardo Burbano

Punto 6
"""
from math import *
from turtle import *

a=input("ingrese el numero de filas de la piramide. ")
a=int(a)

def poli(n):
    for i in range(n):
        forward(2*25*sin(pi/n))
        left(360/n)
        
def fila(lados,filas):
    for i in range(filas):
        poli(lados)
        up()
        forward(50)
        down()    

def piramide(filas):
    for i in range(filas,0,-1):
        fila(i+2,i) 
        up()
        backward((i*60))
        forward(60/2)
        left(90)
        forward(30+30)
        right(90)
        down()
    done()
 
up()
goto(-130,-130)
down()       
piramide(a)

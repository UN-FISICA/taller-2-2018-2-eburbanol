# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 14:22:12 2018

@author: Eduardo Burbano

Punto 5.
"""
from turtle import *

a=input("ingrese el numero de filas de la piramide. Máximo 3 ")
a=int(a)

def poli(n):
    for i in range(n):
        forward(30)
        left(360/n)
        
def fila(lados,filas):
    for i in range(filas):
        poli(lados)
        up()
        forward(60)
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

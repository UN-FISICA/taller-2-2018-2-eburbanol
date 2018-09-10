# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 13:36:18 2018

@author: Eduardo Burbano 

Punto 3
"""

a=input("Ingrese numero de lados del poligono. Minimo 3 ")
a=int(a)
b=input("Ingrese el numero de lados del poligono de alineacion. Minimo 3 ")
b=int(b)

from turtle import *
from math import *

def poli(lado,n):
    for i in range(n):
        forward(lado)
        left(360/n)

def poliguia(l1,l2):
    long=2*25*sin(pi/a)
    lado0=2*130*sin(pi/b) 
    for i in range(l2):
        poli(long,l1)
        left(360*i/l2)
        penup()
        forward(lado0)
        pendown()
        right(360*i/l2)                
    done()
  
penup()
goto(-65,-65)
pendown()
poliguia(a,b)
   
            
done()
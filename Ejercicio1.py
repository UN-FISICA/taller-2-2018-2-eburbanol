# -*- coding: utf-8 -*-
"""
Created on Sun Sep  9 11:36:18 2018

@author: Eduardo Burbano 

Punto 1.
"""
from turtle import *

def cuad(lado):
    for i in range (4):
        for i in range(1):
            penup()  
            forward(10)
            right(90)
            pendown()
            forward(10)
            for i in range (3):                
                right(90)
                pendown()
                forward(20)
            
            right(90)
            forward(10)
            right(270)
        penup()
        forward(110)
        right(90)
cuad(4)
done()
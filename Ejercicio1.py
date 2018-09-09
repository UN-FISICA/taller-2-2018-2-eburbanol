
# -*- coding: utf-8 -*-

"""
By: Eduardo Burbano

Punto 1
"""

from turtle import *

def cuad(n):
    for i in range (4):
        for i in range (2):
            forward (10)
            right (90)
        penup()
        right(180)
        forward(100)
        right(270)
        pendown()
    penup()
    right(90)
    forward(20)
    right(90)
    for i in range(4):
        for i in range (1):            
            pendown()            
            forward(10)
            right(90)
            forward(10)
                          
        penup()
        forward(120)
    penup()
    forward(10)
    right(90)
    forward(10)
    for i in range(4):
        for i in range(1):
            pendown()
            forward(10)
            right(90)
            forward(10)
        right(270)
        penup()
        forward(120)
        right(90)
    
    right(90)
    penup()
    forward(20)
    right(90)
    for i in range(4):
        for i in range(2):
            pendown()
            forward(10)
            right(90)            
        penup()
        forward(120)
        right(270)
        
                        
cuad(4)
done()
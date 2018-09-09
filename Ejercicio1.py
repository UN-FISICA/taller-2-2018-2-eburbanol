
# -*- coding: utf-8 -*-

"""
By: Eduardo Burbano L

Punto 1.
"""

from turtle import *

def cuad(n):
    for i in range (n):
        for i in range (n):
            pendown()
            forward (10)
            right (360/n)
        penup()
        forward(100)
        right(360/n)
        
cuad(4)
done()
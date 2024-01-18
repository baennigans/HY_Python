# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 13:45:17 2024

@author: User
"""
import random
from turtle import *

class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def calcPerimeter(self):
        return 2 * 3.141592 * self.radius
    
    def calcArea(self):
        return 3.141592 * self.radius*self.radius
    
circle = Circle(100)
print("반지름 : ", circle.radius,
      "\n원의 면적 : ", circle.calcArea(),
      "\n원의 둘레 : ", circle.calcPerimeter())
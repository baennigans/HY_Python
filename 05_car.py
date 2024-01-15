# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 11:29:41 2024

@author: User
"""
from turtle import *

class Car:
    def __init__(self, speed, color, fname):
        self.speed = speed
        self.color = color
        self.turtle = Turtle()
        self.turtle.shape(fname)
        
    def drive(self, distance):
        self.turtle.forward(distance)
        
    def stop(self, degree):
        self.turtle.left(degree)
        
register.shape("green.jpg")
            
myCar = Car(60,"green", "green.jpg")
for i in range(4):
    myCar.drive(100)
    myCar.turnleft(90)
# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 17:16:16 2024

@author: User
"""

import random
from turtle import *

class Car:
    def __init__(self, speed, color, fname):
        self.speed = speed
        self.color = color
        self.turtle = Turtle()
        self.turtle.shape(fname)
        self.turtle.speed(self.speed)
        
    def drive(self, distance):
        self.turtle.forward(distance)
        
    def turnleft(self, degree):
        self.turtle.left(degree)
        
register_shape("pink.gif")
            
car_list = []
for _ in range(10):
    car_list.append(Car(random.randint(1, 10), "pink", "pink.gif"))

for _ in range(10):
    for car in car_list:
        car.drive(random.randint(50, 100))
        car.turnleft(random.choice([0, 90, 180, 270]))

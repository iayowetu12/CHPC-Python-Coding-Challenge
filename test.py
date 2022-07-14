#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 22:16:15 2022

@author: sir
"""

class ExampleClass():

    def __init__(self, number):
        self.number = number

    def plus_2_times_4(self,x):
        return(4*(x + 2))

    def arithmetic(self):
        return(self.plus_2_times_4(self.number))

num=ExampleClass(4)
print(num.arithmetic())


class C:
    def __init__(self,a):
        self.a=a
        
    def f(self):
     print(self.a)   
     
ac=C(2)
ac.f()

class Car:
    def __init__(self, color, mileage):
        self.color=color
        self.mileage=mileage
        
    def __str__(self):
        return 'a {self.color} color'.format(self=self)
    
my_car=Car('Blue', 58876)
print(my_car)


import math

class Point(object):
    """A 2D point in the cartesian plane"""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Point({}, {})'.format(self.x, self.y)

    def dist_to_point(self, Point):
        dist = math.sqrt((self.x - Point.x)**2 + (self.y - Point.y)**2)
        return dist

p1 = Point(4,9)
p2 = Point(10,5)
print(p1.dist_to_point(p2))

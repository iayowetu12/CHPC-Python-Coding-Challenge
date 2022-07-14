#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 22:01:35 2022

@author: sir
"""

import math as mt

class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self, Point):
        return mt.sqrt((self.x - Point.x)**2 + (self.y - Point.y)**2)


    def equals(self, Point):
        return (self.x - Point.x) == 0 & (self.y - Point.y) == 0


    def __str__(self):
        return "Point(%d, %d)" % (self.x, self.y)

# Creating Point objects
p1 = Point(4,6)
p2 = Point(6,8)

print('Point 1:', p1)
print('Point 2:', p2)

if p1.equals(p2):
    print('Points are equals')
else:
    print('Point are not equals')

d = p1.distance(p2)
print('Distance between points are',d)
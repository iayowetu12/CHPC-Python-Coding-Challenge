#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 06:41:17 2022

@author: sir
"""

class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age=age
        print('Person constructor')
    
    def my_name_is(self):
        print('My name is ' + self.name)
        
        
        
class Athlete(Person):
    
    def __init__(self, teacher, name, age):
        super().__init__(name, age)
        self.teacher = teacher
        print('Athlete constructor')
        
        
    def my_name_is(self):
        print('My name is ' + self.teacher)
        
        
class Student(Athlete):
    
    def __init__(self, name, age, student_id, gpa, teacher):
        super().__init__(teacher, name, age)
        self.student_id = student_id
        self.gpa = gpa
        print('Student constructor')
        print(self.name)
        # Athlete.__init__(self, teacher)
        # Athlete.my_name_is(self)
        # super().my_name_is()
        
        
        
std= Student('WittCode',25,1,4, 'Professor WittCode')
print(std.name)
print(std.student_id)
print(std.gpa)
print(std.age)
std.my_name_is()
        
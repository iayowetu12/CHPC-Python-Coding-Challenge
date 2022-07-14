
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  3 09:03:21 2022

@author: sir
"""

import math

class Rocket():
    # Rocket simulates a rocket ship for a game,
    
    def __init__(self, x=0, y=0):
        # Q1. Provide the code to initialize the self variables
        self.x=x
        self.y=x

    def move_up(self): 
        # Q2. Provide the code to increment the y-position of the rocket by 1
         self.y += 1

    # Q3. Write a new method that decrements the y-position of the rocket by 9.89
    def move_down(self):
        self.y -=9.89

    def move_rocket(self, x_increment=0, y_increment=1):
        # Q4. Provide code to move the rocket according to the input paremeters given.
        self.x += x_increment
        self.y += y_increment

    def get_distance(self, other_rocket):
        # Q5. Provide code to calculats the distance from this rocket to another rocket,
        #  and returns that value.
        distance = math.sqrt((self.x-other_rocket.x)**2+(self.y-other_rocket.y)**2)
        return distance
        
        
        
# Make a series of rockets at different starting places.
rockets = []
rockets.append(Rocket())
rockets.append(Rocket(0,10))
rockets.append(Rocket(100,0))

# Q6. Provide code using a loop to show x and y coordinates of each rocket.
# for x in range(0,5):
#     rockets.append(Rocket())
for i, rocket in enumerate(rockets):
    print("Rocket %d is at (%d, %d)." % (i, rocket.x, rocket.y))

# Move each rocket a different amount.
rockets[0].move_rocket()
rockets[1].move_rocket(10,10)
rockets[2].move_rocket(-10,0)

# Q7. Provide code using a loop to show x and y coordinates of each rockets new position
for i, rocket in enumerate(rockets):
    print("Rocket %d is at (%d, %d)." % (i, rocket.x, rocket.y))


# Q8. Show the distance between the first and second rocket
#rocket1=Rocket()
#rocket2=Rocket(14,7)
distance_between=rockets[0].get_distance(rockets[1])
print("The rockets distance apart: %f" % distance_between)

# Q9. Show the distance between the first and third rocket
#rocket1=Rocket()
#rocket3=Rocket(3,7)
distance_between=rockets[0].get_distance(rockets[2])
print("The rockets distance apart: %f" % distance_between)

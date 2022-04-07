import numpy as np
from skyfield.api import load
objects = load('de421.bsp')

#Function which returns the current distance between two objects.
def distance(object1, object2):
    body1 = objects[object1]
    body2 = objects[object2]
    time = load.timescale().now()
    position = body1.at(time).observe(body2)
    distance = position.distance()
    return(distance)

#Requests user input on which two objects to check distance.
print("Welcome")
listreq = input("Would you like a list of available object? (Y/N)")
if listreq.lower() == 'y':
    print(objects)

object1 = input("Enter your first Solar body:")
object2 = input("Enter your second Solar body:")
print(distance(object1, object2))

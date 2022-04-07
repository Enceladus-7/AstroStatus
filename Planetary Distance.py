import numpy as np
from skyfield.api import load

def distance(object1, object2):
    objects = load('de421.bsp')
    body1 = objects[object1]
    body2 = objects[object2]
    time = load.timescale().now()
    position = body1.at(time).observe(body2)
    distance = position.distance()
    return(distance)

print("Welcome")
object1 = input("Enter your first Solar body:") + ' BARYCENTER'
object2 = input("Enter your second Solar body:") + ' BARYCENTER'
print(distance(object1, object2))

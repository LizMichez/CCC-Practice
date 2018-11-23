# This program gives the circumference of the circle when
# given its radius

import math

radius = int(input("Radius of circle:"))
units = input("units:")

circumference = 2 * math.pi * radius

print("The circumference of the circle is", circumference, units)

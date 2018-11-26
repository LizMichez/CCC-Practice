# This code just solves the pythagorean theorem
import math  # This line imports the math libraries

a = int(input("Input a value for 'a': "))  # Declares var a as an integer based on user input
b = int(input("Input a value for 'b': "))  # Declares var b as an integer based on user input

c = math.sqrt(a ** 2 + b ** 2)  # Declares var c based on math involving a and b

print("The hypotenuse is", c, "cm long.")  # Prints the output

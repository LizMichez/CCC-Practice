# This things gives you when easter is given the year and a very uh interesting formula

year = int(input("What year is this easter in? "))  # Declares var years based on user input

z = year % 19  # Declares the variable z for math
y = year / 100  # Declares the variable y for math
x = year % 100  # Declares the variable x for math
w = y / 4  # Declares the variable w for math
v = y % 4  # Declares the variable v for math
u = (8 * y + 13) / 25  # Declares the variable u for math
t = (19 * z + y - w - u + 15) % 30  # Declares the variable t for math
s = (z + 11 * t) / 319  # Declares the variable s for math
r = x / 4  # Declares the variable r for math
q = x % 4  # Declares the variable q for math
p = (2*v + 2*r - t - s - q + 32) % 7  # Declares the variable p for math

month = round((t - s + p + 90) / 28)  # Declares the variable month based on the math
day = round((t - s + p + month + 19) % 32)  # Declares the variable day based on the math

monthsOfYear = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
# The array above lists the days of the year

monthStr = monthsOfYear[month-1]  # Declares the variable monthStr as the value at the "months" place in monthsOfYear

print("Easter is on", monthStr, day)  # Prints when easter is on

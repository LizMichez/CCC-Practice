# This code breaks up a three digit number and outputs the hundreds, tens, and ones

num = input("Input three digit number: ")  # Declares srt num based on user input
i = 0  # Declares var i as 0

while i < len(num):  # Opens while loop
    print(num[i] + "0"*(len(num)-(i+1)))  # Prints the value at index i plus the number of 0 appropriate
    i = i+1  # Adds one to i

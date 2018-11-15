import math

getNum = int(input("How many numbers will be entered?"))
numbers = [0] * getNum
index = 0

while index < getNum:
    numbers[index] = int(input("Enter number"))
    index += 1

for x in numbers:
    print(x)
    firstInt = x
    while len(str(x)) > 2:
        lastNum = int(int(x) % 10)
        x = math.floor(x // 10) - lastNum
        print(x)

    if x == 11:
        print("The number", firstInt, "is divisible by 11.")
    else:
        print("The number", firstInt, "is not divisible by 11.")

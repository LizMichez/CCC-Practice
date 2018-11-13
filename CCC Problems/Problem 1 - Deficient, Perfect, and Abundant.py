getNum = int(input("How many numbers will be entered?"))
numbers = [0] * getNum
index = 0

while index < getNum:
    numbers[index] = int(input("Enter number"))
    index += 1

index = 0

for x in numbers:
    divideBy = 1
    sumOfd = 0
    while divideBy < x:
        if x % divideBy == 0:
            sumOfd += divideBy
        divideBy += 1

    if sumOfd == x:
        print(x, "is a perfect number.")
    elif sumOfd < x:
        print(x, "is a deficient number.")
    elif sumOfd > x:
        print(x, "is an abundant number.")

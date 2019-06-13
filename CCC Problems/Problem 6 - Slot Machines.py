coins = int(input("Input number of quarters: "))
m1 = int(input("Input number of plays in machine 1: "))
m2 = int(input("Input number of plays in machine 2: "))
m3 = int(input("Input number of plays in machine 3: "))
plays = 0


def oneTurn():
    global coins
    global plays
    coins -= 1
    plays += 1


while coins > 0:
    oneTurn()
    m1 += 1
    if m1 % 35 == 0:
        coins += 30
    elif coins == 0:
        break

    oneTurn()
    m2 += 1
    if m2 % 100 == 0:
        coins += 60
    elif coins == 0:
        break

    oneTurn()
    m3 += 1
    if m1 % 10 == 0:
        coins += 9
    elif coins == 0:
        break

print("Martha plays ", plays, " times before going broke.")

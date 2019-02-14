import itertools

getNum = str(input("Enter starting day and month length: ")).split()

weekDay = int(getNum[0])
lastDay = int(getNum[1])
days = ['   ' * (weekDay-1) + ' ' * (weekDay-2)]

print('Sun Mon Tue Wed Thr Fri Sat')

for subset in itertools.count(start=1, step=1):
    if int(subset) <= lastDay:
        if int(subset) == 1 and weekDay == 1:
            days.append(' ' * (3-len(str(subset))) + str(subset))
        elif (int(subset)+(weekDay-2)) % 7 == 0:
            days.append('\n' + ' ' * (3-len(str(subset))) + str(subset))
        else:
            days.append(' ' + ' ' * (3-len(str(subset))) + str(subset))
    else:
        break

print(''.join(days))

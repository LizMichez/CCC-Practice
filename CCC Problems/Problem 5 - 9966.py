import itertools

getNums = str(input('Input range of numbers: ')).split()

start = int(getNums[0])
finish = int(getNums[1])
flippables = 0

for subset in itertools.count(start=start, step=1):
    if (str(subset).count('2') == 0) and (str(subset).count('3') == 0) and (str(subset).count('4') == 0) and (str(subset).count('5') == 0) and (str(subset).count('7') == 0) and (subset <= finish):
        flipped = str(subset)[::-1]
        flipped = flipped.replace('6', 'a')
        flipped = flipped.replace('9', '6')
        flipped = flipped.replace('a', '9')
        if flipped == str(subset):
            flippables = flippables + 1

    elif subset >= finish:
        break

print(flippables)
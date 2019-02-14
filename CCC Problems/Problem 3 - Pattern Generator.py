# Input comes in form n k with one space between and k always being less than n
import itertools


def unique(list1):
    list_set = set(list1)
    unique_list = list(list_set)
    for x in unique_list:
        print(x)


brokeNums = (str(input("Input Numbers: "))).split()
n = int(brokeNums[0])
k = int(brokeNums[1])
allBits = []

firstBits = (['0'] * (n-k)) + (['1'] * k)
for subset in itertools.permutations(firstBits, len(firstBits)):
    allBits.append(''.join(subset))

unique(allBits)

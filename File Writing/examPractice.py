def postalValidation(postalCode):
    file = open("postal_codes.txt", "r")
    postal = ""

    for x in postalCode:
        if x.isalpha():
            postal += x.lower()
        else:
            postal += x

    print(postal)

    if len(postal) >= 3:
        for line in file:
            de_line = str(line[0].lower() + str(line[1]) + line[2].lower())
            if de_line == postal[0:3]:
                file.close()
                return True
    file.close()
    return False


def isAutomorphic(num1):
    try:
        square = num1**2
        num = str(num1)

        if str(square)[-len(num):] == num:
            return True
        else:
            return False
    except ValueError:
        return "You must enter a number"


def evenDigs(lower, upper):
    try:
        if lower % 2 != 0:
            lower += 1

        nums = []
        [nums.append(x) for x in range(lower, upper, 2)]
        return str(nums)[1:-1]

    except TypeError:
        return "Both inputs must be numbers, with lower less than upper"


def dirReduc(dir):  # Returns simplified directions imputed as a list e.g. ["WEST", "EAST", "WEST"] --> ["WEST"]
    final = []
    dir = str(dir)
    print(dir)

    side = dir.count("WEST") - dir.count("EAST")
    vert = dir.count("SOUTH") - dir.count("NORTH")

    if side < 0:
        while side != 0:
            final.append("EAST")
            side += 1
    else:
        while side != 0:
            final.append("WEST")
            side -= 1

    if vert < 0:
        while vert != 0:
            final.append("EAST")
            vert += 1
    else:
        while vert != 0:
            final.append("WEST")
            vert -= 1

    return final


def rot13(message):
    alpha = "abcdefghijklmnopqrstuvwxyzabcdefghijklm"
    final = ""

    for x in message:
        if x.isalpha():
            if x.isupper():
                final += alpha[alpha.index(x.lower())+13].upper()
            else:
                final += alpha[alpha.index(x) + 13]
        else:
            final += x

    return final


def is_pangram(s):  # checks if phrase has the entire alphabet in it
    alpha = "abcdefghijklmnopqrstuvwxyz"
    num = 0
    for x in alpha:
        if x in s.lower():
            num += 1
    return num == 26


def tribonacci(sig, n):  # Makes a fibonachi sequence adding three not two
    for x in range(2, n-1):
        sig += [sig[x-2] + sig[x-1] + sig[x]]
    return sig[0:n-1]


def sort_array(source_array):  # sorts all odd numbers in an array, leaving even where they are
    ordered = []
    for x in source_array:
        if x % 2 != 0 and x != 0:
            ordered += [x]
    ordered.sort()

    for x in source_array:
        if x % 2 == 0 or x == 0:
            ordered.insert(source_array.index(x), x)
    return ordered


print(sort_array([5, 3, 2, 8, 1, 4]))

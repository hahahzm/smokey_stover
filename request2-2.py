import time
import math

def ternary(x, m):
    i = 0
    a = x
    while (a != 0):
        b = a % 3
        a = a / 3
        if (i == m):
            return b
        i = i + 1
    return 0

def answer(x):
    # your code here
    base = []
    a = x
    modulo = 3
    offset = 1

    power = int(math.ceil(math.log(2 * a + 1,3)))
    
    
    for i in range(0, power):
        b = ternary(x + offset, i)
        base.append(b - 1)
        offset = offset + modulo
        modulo = modulo * 3
        a = a / 3

    result = []

    for number in base:
        if (number == 1):
            result.append("R")
        elif (number == -1):
            result.append("L")
        else:
            result.append("-")
    return result


while True:
    a = int(input("Enter: "))
    print answer(a)

# https://goo.gl/GslGD3

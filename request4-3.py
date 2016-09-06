import math
import operator
import itertools
import sys

sys.setrecursionlimit(1024)

cache = dict()

def satisfy(l, n):
    result = True
    sum = 0
    for num in l:
        if num == -1:
            if sum == 0:
                result = False
                break
            elif sum == (n - 1):
                result = False
                break
        elif num == 1:
            if sum == (n - 1):
                result = False
                break
        sum += num
    if sum != (n - 1):
        result = False
    return result

def pd(distribution, t):
    ct = -t
    for i in range(-t, t + 1):
        print "%5d " % i,
    print
    for i in distribution:
        print "%5d " % i,
    print

def dp(t, n):
    solution = []
    for i in range(0, t + 1):
        row = []
        for j in range(0, n + 1):
            row.append(0)
        solution.append(row)

    for i in range(1, t + 1):
        for j in range(1, n + 1):
            value = 0
            if i == (j - 1):
                value = 1
            elif (j == 1):
                value = 1
            elif i > (j - 1):
                value = solution[i-1][j-1] + solution[i-1][j] + solution[i-1][j+1]
            solution[i][j] = value

    return solution

def readCacheDP(i,j):
    if (i,j) in cache:
        return cache[i,j]
    else:
        return 0

def dp5(t, n):
    for i in range(1, t + 1):
        for j in range(1, n + 1):
            value = 0
            if i == (j - 1):
                value = 1
            elif (j == 1):
                value = 1
            elif i > (j - 1):
                value = readCacheDP(i-1,j-1)+readCacheDP(i-1,j)+readCacheDP(i-1,j+1)
            if (value != 0):
                cache[i,j] = value % 123454321


def dp2(a,b,c,n):
    if (a < 0 or b < 0 or c < 0):
        return 0
    if (a,b,c) in cache:
        return cache[a,b,c]
    pt = n - a + b
    value = 0
    if pt < 1 or pt > n:
        value = 0
    elif pt == n:
        if a == 0:
            value = 1
        else:
            value = 0
    else:
        #at some middle squares
        value = dp2(a-1,b,c,n)+dp2(a,b-1,c,n)+dp2(a,b,c-1,n)

#    print "%d %d %d %d | " % (a,b,c,n), 
#    print value
    value = value % 123454321
    cache[a,b,c] = value
    return value

def readCache(i,j,k):
    if (i,j,k) in cache:
        return cache[i,j,k]
    else:
        return 0

def dp3(t,n):
    for i in range(n - 1, t + 1):
        for j in range(0, i - n + 2):
            for k in range(0, t - i - j + 1):
                if (i + j + k) > t:
                    continue
                pt = n - i + j
                value = 0
                if pt < 1 or pt > n:
                    value = 0
                elif pt == n:
                    if i == 0:
                        value = 1
                    else:
                        value = 0
                else:
                    #at some middle squares
                    value = readCache(i-1,j,k)+readCache(i,j-1,k)+readCache(i,j,k-1)

                cache[i,j,k] = value % 123454321

def dp4(t,n):
    result = 0

    i = n - 1

    while True:
        j = i + 1 - n
        k = t - i - j
        if k < 0:
            break
        else:
            result += dp2(i,j,k,n)
        i += 1
    return result

def printCache(t,n):
    for k in range(0, t - n):
        for i in range(n - 1, t + 1):
            for j in range(0, t - n + 2):
                print "%3d " % readCache(i,j,k),
            print 
        print "=============================="
    result = 0
    a = n - 1
    while True:
        b = a + 1 - n
        c = t - a - b
        if c < 0:
            break
        else:
            result += readCache(a,b,c)
            result = result % 123454321
        a += 1

    return result % 123454321


def answer(t, n):
    # your code here
    count = 0
    distribution = []
    for i in range(0, 2*t + 1):
        distribution.append(0)

    for sequence in itertools.product([-1, 0, 1], repeat = t):
        distribution[t + sum(sequence)] += 1
        if (satisfy(sequence, n)):
            count += 1

    #pd(distribution, t)
    return count




t = int(raw_input("t: "))
n = int(raw_input("n: "))

dp5(t, n)

#print "=================================="
#for i in range(0, t + 1):
#    for j in range(1, n + 1):
#        print "%4d" % (dp4(i,j)),
#    print 

print "=================================="
#for i in range(0, t + 1):
#    for j in range(1, n + 1):
 #       print "%4d" % (sol[i][j]),
#    print 
#print answer(t,n)
print cache[t,n]
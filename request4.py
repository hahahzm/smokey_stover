import math
import operator

cache = dict()
solution = dict()

def combination(n, r):
    if n < r: return 0
    r = min(r, n-r)
    if r == 0: return 1
    if (n,r) in cache:
        return cache[n,r]
    numer = reduce(operator.mul, xrange(n, n-r, -1))
    denom = reduce(operator.mul, xrange(1, r+1))
    result = numer//denom
    cache[n,r] = result
    return result

def answer0(N, K):
    if (N, K) in solution:
        return solution[N, K]
    right = N * (N - 1) // 2
    result = 0
    if K < (N - 1) or K > right:
        result = 0
    elif (k == (N - 1)):
        result = long(math.pow(N, N - 2))
    else:
        sum1 = 0
        for m in range(0, N - 1):
            sum2 = 0
            left = max(0, K - (m + 1) * m // 2)
            for p in range(left, K - m + 1):
                sum2 += combination((N - 1 - m) * (N - 2 - m) // 2, p) * answer0(m + 1, k - p)
            sum1 += combination(N - 1, m) * sum2
        result = combination((N * (N - 1) // 2), k) - sum1
    solution[N, K] = result

    return result

def answer(N, K):
    return str(answer0(N, K))


while True:
    n = int(raw_input("n: "))
    k = int(raw_input("k: "))
    print answer(n,k)
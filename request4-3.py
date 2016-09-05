import math
import operator
import itertools

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

def answer(t, n):
    # your code here
    sum = 0
    for sequence in itertools.product([-1, 0, 1], repeat = t):
    	if (satisfy(sequence, n)):
    		sum += 1
    return sum

print answer(1, 2)
from math import *

cache = dict()

def generate(limit):
	arr = [1,1,2]
	for i in range(3, limit):
		k = i // 2
		if i % 2 != 0:
			arr.append(arr[k - 1] + arr[k] + 1)
		else:
			arr.append(arr[k] + arr[k + 1] + k)
	return arr

def fibonacci(limit):
	arr=[1,1]
	for i in range(2, limit):
		arr.append(i+arr[i-1]+arr[i-2])
	return arr

def getValue(n):
	if (n) in cache:
		return cache[n]
	value = 1
	if n == 0 or n == 1:
		value = 1
	elif n == 2:
		value = 2
	else:
		if n % 2 == 0:
			value = getValue(n//2) + getValue(n//2+1)+n//2
		else:
			value = getValue(n//2) + getValue(n//2-1)+1
	cache[n] = value
	return value

def answer(str_S):
	target = int(str_S)

	a = 0
	# max for b: 1000000000000000000000000
	b = 1000000000000000000000000
	va1 = -1
	while a < (b - 2):
		print "Range: [%3d,%3d]" % (a,b)
		c = (a + b) // 2

		c = c if c % 2 == 0 else c - 1

		x = getValue(a)
		if x == target:
			va1 = a
			break
		y = getValue(b)
		if y == target:
			va1 = b
			break
		z = getValue(c)
		if z == target:
			va1 = c
			break

		if z > target:
			b = c
		if z < target:
			a = c

	if a == (b-2):
		if getValue(a+1) == target:
			va1 = a+1

	va2 = -1
	a = 1
	b = 1000000000000000000000000 - 1
	while a < (b-2):
		print "Range: [%3d,%3d]" % (a,b)
		c = (a + b) // 2

		c = c if c % 2 != 0 else c - 1

		x = getValue(a)
		if x == target:
			va2 = a
			break
		y = getValue(b)
		if y == target:
			va2 = b
			break
		z = getValue(c)
		if z == target:
			va2 = c
			break

		if z > target:
			b = c
		if z < target:
			a = c

	if a == (b-2):
		if getValue(a+1) == target:
			va1 = a+1

	if va1 == -1 and va2 == -1:
		return "None"

	return str(va1) if va1 > va2 else str(va2)


while True:
	n = int(raw_input("n: "))
	value = getValue(n)
	print value
	print answer(str(value))
from sympy import *

count = 0
list = []
while count < 2000000:
	if isprime(count) == True:
		list.append(count)
	count += 1

total = 0

for num in list:
	total += num

print(total)
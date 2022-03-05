import random
from math import sqrt
check = True

while check:
	a = random.randint(200,500)
	b = random.randint(200,500)
	if b > a:
		b = random.randint(200,500)
	output = a**2 + b**2
	c = round(sqrt(output))
	if c < b or c < a:
		continue
	if c**2 != a**2 + b**2:
		continue
	if a + b + c == 1000:
		print(a * b * c)
		break
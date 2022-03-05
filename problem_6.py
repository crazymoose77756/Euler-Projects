square_num = 1
output = 0

while square_num < 101:
	squared = square_num * square_num
	output += squared
	square_num += 1
print(output)

counter = 0
total = 0
while counter < 100:
	total += counter+1
	counter += 1 

total = total * total
print(total)

diff = total - output
print(diff)
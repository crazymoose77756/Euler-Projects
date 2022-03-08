#Evaluate the sum of all the amicable numbers under 10000.


number = 220
my_sum = 0

for num in range(1,number+1):
	if number % num == 0:
		my_sum += num

amic = my_sum-number
print(amic)
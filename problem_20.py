number, product, my_sum = 100, 1, 0

for digs in range(1,number+1):
	product *= digs

my_list = list(str(product))

for number in my_list:
	my_sum += int(number)

print(my_sum)
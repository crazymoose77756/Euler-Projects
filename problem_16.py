my_list = []
my_sum = 0
big_num = str(2**1000)

for char in range(0,len(big_num), 1):
	my_list.append(big_num[char:char+1])

for num in my_list:
	my_sum += int(num)

print(my_sum)
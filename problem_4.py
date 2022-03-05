ran_num_one = 100
ran_num_two = 99
check = True
prev = 0

while check:
	ran_num_two += 1
	num = ran_num_one * ran_num_two
	if str(num)[::-1] == str(num):
		pali_list.append(num)
		if num > prev:
			print("New best: " + str(num) + " came from " + str(ran_num_one) + " " + str(ran_num_two))
			prev = num
	if ran_num_two == 999:
		ran_num_two = 99
		ran_num_one += 1
	elif ran_num_one == 999:
		check = False

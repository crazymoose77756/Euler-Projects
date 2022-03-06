def check():
	num = 76576400
	list = []
	check = True

	while check:
		for i in range(1, num + 1):
			if num % i == 0:
				list.append(i)

		length = len(list)
		if length != 500:
			list = []
			print("Checked " + str(num))
			num += 1
		else:
			end = time.time()
			break

	print("There are " + str(length) + " factors for " + str(num))
	print(list[0])

check()
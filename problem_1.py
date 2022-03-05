def main():
	make_100_list()
	determine()
	make_sum()

num_list = []
right_list = []

def make_100_list():
	x = 0
	while x < 1000:
		num_list.append(x)
		x += 1

def determine():
	for num in num_list:
		if num % 3 == 0 or num % 5 == 0:
			right_list.append(num)

def make_sum():
	sum = 0
	for num in right_list:
		sum = sum + num
	print(sum)

main()


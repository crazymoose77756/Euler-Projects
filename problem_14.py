import time

start = time.time()
curr_big, big_num = 0, 0

def get_num(number):
    count = 1
    number1 = number
    while number1 != 1:
        if number1 % 2 == 0:
            number1 /=2
            count += 1
        else:
            number1 = (3*number1) + 1
            count += 1
    return count, number

for i in range(1, 1000000):
	count, number = get_num(i)
	if count > curr_big:
		curr_big, big_num = count, number

print("The number is " + str(big_num) + ". Took: " + str(int(time.time()-start)) + " seconds")
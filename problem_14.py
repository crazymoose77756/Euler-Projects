import time

start = time.time()
fullList = []

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
    return [count, number]

for i in range(1, 1000000):
	fullList.append(get_num(i))

sortedList = sorted(fullList, reverse = True)
print(*sortedList[:1])
print("Time: " + str(int(time.time()-start)) + " seconds")
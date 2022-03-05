import time

def prime(x):
	if x <= 1:
		return False

	for counter in range(2, x):
		if x % counter == 0:
			return False

	return True

def main():
	start = time.time()
	prime_index = 1
	counter = 1
	while prime_index <= 10001:
		if prime(counter):
			if prime_index == 10001:
				print(counter)
				end = time.time()
				print("Took: " + str(end - start) + " seconds")
			prime_index += 1
		counter += 1

main()
dic = {n:0 for n in range(0,1001)}

dic[0] = 0
dic[1] = dic[2] = dic[6] = dic[10] = 3
dic[4] = dic[5] = dic[9] = 4
dic[50] = dic[60] = dic[40] = dic[3] = dic[7] = dic[8] = 5
dic[20] = dic[30] = dic[11] = dic[12] = dic[80] = dic[90] = 6
dic[15] = dic[16] = dic[70] = 7
dic[18] = dic[19] = dic[14] = dic[13] = 8
dic[17] = 9
dic[1000] = 11

for i in range(21,100):
	tens = int(i/10)*10
	ones = i - tens
	dic[i] = dic[tens]+dic[ones]

for i in range(100,1000):
	hundreds = int(i/100)
	tens_ones = i - hundreds*100
	if tens_ones == 0:
		dic[i] = dic[hundreds] + 7
	else:
		dic[i] = dic[hundreds] + 10 + dic[tens_ones]

print(sum(dic.values()))
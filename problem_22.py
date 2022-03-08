file = open("p022_names.txt","r")
sorted_list = sorted(file.read().replace('"',"").split(","))

total_val = 0
char_dict={"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8,"I":9,"J":10,"K":11,"L":12,"M":13,"N":14,"O":15,"P":16,"Q":17,"R":18,"S":19,"T":20,"U":21,"V":22,"W":23,"X":24,"Y":25,"Z":26}

for name in sorted_list:
	name_val, pos_val = 0, 1
	name_chars = list(name)

	pos_val += sorted_list.index(name)

	for char in name_chars:
		name_val += char_dict[char]

	total_val += pos_val * name_val

print(total_val)
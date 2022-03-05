result = 0
check = True

while check:
    result += 20
    for x in [20, 19, 18, 17, 16, 15, 14, 13, 11]:
        if result % x != 0:
            break
    else:
       check = False

print('Result: ', result)
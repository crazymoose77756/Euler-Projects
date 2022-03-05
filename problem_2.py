prev = 0
cur = 1
total = 0
while True:
    prev = cur
    cur = prev + cur
    if cur >= 4000000:
        break
    if cur % 2 == 0:
        total += cur
print(total)
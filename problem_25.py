steps = 100000
prev, curr, count = 0, 1, 0

while count < steps:
   next_num = prev + curr
   prev = curr
   curr = next_num
   count += 1

   if len(str(prev)) == 1000:
        print(count)
        break
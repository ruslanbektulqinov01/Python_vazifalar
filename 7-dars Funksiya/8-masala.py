def Even(k):
    return k % 2 == 0
count = 0
for i in range(1, 11):
   if Even(i):
       print(i, "juft son")
       count += 1
   if count == 5:
       break
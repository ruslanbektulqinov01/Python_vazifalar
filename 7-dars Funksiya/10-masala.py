def IsPowerS(k):
   return any(k == 5 ** i for i in range(1, 11))
count = 0
for i in range(1, 11):
   if IsPowerS(i):
       print(i)
       count += 1
   if count == 2:
       break
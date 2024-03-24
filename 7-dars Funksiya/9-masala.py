def IsSquare(k):
   return (k ** 0.5).is_integer()
count = 0
for i in range(1, 11):
   if IsSquare(i):
       print(i, "tola kvadrat son")
       count += 1
   if count == 2:
       break


def sign(x):
   if x < 0:
       return -1
   elif x == 0:
       return 0
   else:
       return 1
a = -3
b = 3
result_a = sign(a)
result_b = sign(b)
print(result_a)
print(result_b)

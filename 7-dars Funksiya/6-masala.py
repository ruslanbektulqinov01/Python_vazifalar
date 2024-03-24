def Calc(a, b, op):
  if op == 1:
       return a - b
   elif op == 2:
       return a * b
   elif op == 3:
       if b != 0:
           return a / b
       else:
           return
   else:
       return a + b
a = 6
b = 3
n1 = Calc(a, b, 1)
n2 = Calc(a, b, 2)
n3 = Calc(a, b, 3)
print(n1)
print(n2)
print(n3)

def Range(A, B):
  if A > B:
      return 0
  else:
      total_sum = 0
      for i in range(A, B + 1):
          total_sum += i
      return total_sum

a = 3
b = 8
c = 5

sum_ab = Range(a, b)
sum_bc = Range(b, c)

print(sum_ab)
print(sum_bc)


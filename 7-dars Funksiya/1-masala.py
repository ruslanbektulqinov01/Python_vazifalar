def sign(x):
    return -1 if x < 0 else 0 if x == 0 else 1

a = -3
b = 3

result_a = sign(a)
result_b = sign(b)

print(result_a)
print(result_b)


n = int(input("n ni kiriting (musbat butun son): "))

k = 1
while k * k <= n:
    k += 1

k -= 1

print(f"Kvadrati n dan katta bo‘lmagan eng katta butun k soni: {k}")

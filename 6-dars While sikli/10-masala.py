n = int(input("n ni kiriting (1 dan katta musbat butun son): "))

k = 1
while k ** 3 < n:
    k += 1

k -= 1

print(f"3 ning darajasida k < n tengsizlik o'rinli bo'ladigan eng katta k: {k}")

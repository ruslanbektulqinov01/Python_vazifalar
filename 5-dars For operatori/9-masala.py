a = int(input("a sonini kiriting: "))
b = int(input("b sonini kiriting: "))

yigindisi = sum(x ** 2 for x in range(a, b + 1))

print(f"{a} dan {b} gacha bo'lgan sonlarning kvadratlar yig'indisi: {yigindisi}")

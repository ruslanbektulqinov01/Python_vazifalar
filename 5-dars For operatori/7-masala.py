#2 ta a va b butun sonlar berilgan. (a<b) a dan b gacha bo‘lgan butun sonlar yig‘indisi topilsin

a = int(input("a sonini kiriting: "))
b = int(input("b sonini kiriting: "))

yigindisi = sum(range(a, b + 1))

print(f"{a} dan {b} gacha bo‘lgan butun sonlar yig‘indisi: {yigindisi}")

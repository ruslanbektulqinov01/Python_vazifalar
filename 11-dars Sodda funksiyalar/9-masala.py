def raqamlar_yigindisi_kopaytmasi(son):

    yigindi = sum(int(x) for x in str(son))

    kopaytma = 1
    for x in str(son):
        kopaytma *= int(x)

    return yigindi, kopaytma

son = int(input("Uch xonali butun sonni kiriting: "))

yigindi, kopaytma = raqamlar_yigindisi_kopaytmasi(son)

print("Raqamlar yig'indisi:", yigindi)
print("Raqamlar ko'paytmasi:", kopaytma)

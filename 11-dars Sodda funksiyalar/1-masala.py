def topish(a, b):
    yigindi = a + b
    ayirma = a - b
    kopaytma = a * b
    nisbat = a / b

    return yigindi, ayirma, kopaytma, nisbat

a = float(input("Birinchi sonni kiriting: "))
b = float(input("Ikkinchi sonni kiriting: "))

yigindi, ayirma, kopaytma, nisbat = topish(a, b)
print("Yig'indisi:", yigindi)
print("Ayirmasi:", ayirma)
print("Ko'paytmasi:", kopaytma)
print("Nisbati:", nisbat)

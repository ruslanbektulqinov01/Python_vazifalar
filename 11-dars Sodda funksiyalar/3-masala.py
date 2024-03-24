import math
def aylananing_uzunligi_va_yuzi(R):
    L = 2 * math.pi * R
    S = math.pi * R ** 2
    return L, S

R = float(input("Doira radiusini kiriting: "))

uzunlik, yuzi = aylananing_uzunligi_va_yuzi(R)

print("Aylananing uzunligi:", uzunlik)
print("Doiraning yuzi:", yuzi)

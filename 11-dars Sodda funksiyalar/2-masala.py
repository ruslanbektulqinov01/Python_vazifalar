import math
def uchburchak_yuzi_perimetri(a, b):
    S = 0.5 * a * b

    c = math.sqrt(a ** 2 + b ** 2)

    P = a + b + c

    return S, P

a = float(input("Uchburchakning birinchi katetini kiriting (a): "))
b = float(input("Uchburchakning ikkinchi katetini kiriting (b): "))

S, P = uchburchak_yuzi_perimetri(a, b)
print("Uchburchakning yuzi:", S)
print("Uchburchakning perimetri:", P)

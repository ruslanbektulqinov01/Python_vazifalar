import math
def orta_arifmetik(a, b):
    return (a + b) / 2
def orta_geometrik(a, b):
    return math.sqrt(a * b)

a = float(input("Birinchi sonni kiriting: "))
b = float(input("Ikkinchi sonni kiriting: "))

orta_arifmetik_qiymat = orta_arifmetik(a, b)
orta_geometrik_qiymat = orta_geometrik(a, b)

print("Ortacha arifmetik qiymat:", orta_arifmetik_qiymat)
print("Ortacha geometrik qiymat:", orta_geometrik_qiymat)

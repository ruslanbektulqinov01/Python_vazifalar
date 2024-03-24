# O'rta arifmetikni topish uchun funktsiya
def orta_arifmetik(sonlar):
    return sum(sonlar) / len(sonlar)

# Misol sonlar
sonlar_misol = [15, 5]

# O'rta arifmetikni hisoblash
natija = orta_arifmetik(sonlar_misol)

# Natijani ekranga chiqarish
print(f"Berilgan sonlar: {sonlar_misol}")
print(f"O'rta arifmetik: {natija}")



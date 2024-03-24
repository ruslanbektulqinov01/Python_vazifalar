a = int(input("a ni kiriting (musbat son): "))
b = int(input("b ni kiriting (musbat son, a dan katta): "))

kesma_son = 0
qolgan_bolagi = a

while qolgan_bolagi >= b:
    kesma_son += 1
    qolgan_bolagi -= b

print(f"{a} uzunlikdagi kesmaga {b} uzunlikdagi kesmani joylashtirganda, eng ko'p miqdorda joylashtirilgan kesma uzunligi: {kesma_son}, va bo'sh qolgan bo'lagi uzunligi: {qolgan_bolagi}")

def tortburchak_yuzi(x1, y1, x2, y2):
    uzunlik1 = abs(x2 - x1)
    uzunlik2 = abs(y2 - y1)
    yuzi = uzunlik1 * uzunlik2
    return yuzi

x1, y1 = map(float, input("Birinchi diagonallarning boshlanishi uchun koordinatalarni kiriting (x1, y1): ").split())
x2, y2 = map(float, input("Ikkinchi diagonallarning boshlanishi uchun koordinatalarni kiriting (x2, y2): ").split())

yuzi = tortburchak_yuzi(x1, y1, x2, y2)
print("To'g'ri to'rtburchakning yuzi:", yuzi)

def uchburchak_yuzi(A, B, S):
    x1, y1 = A
    x2, y2 = B
    x3, y3 = S

    S = 0.5 * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    return S

x1, y1 = map(float, input("A nuqtasining koordinatalarini kiriting (x1, y1): ").split())
x2, y2 = map(float, input("B nuqtasining koordinatalarini kiriting (x2, y2): ").split())
x3, y3 = map(float, input("S nuqtasining koordinatalarini kiriting (x3, y3): ").split())

A = (x1, y1)
B = (x2, y2)
S = (x3, y3)

area = uchburchak_yuzi(A, B, S)
print("Uchburchak yuzi:", area)

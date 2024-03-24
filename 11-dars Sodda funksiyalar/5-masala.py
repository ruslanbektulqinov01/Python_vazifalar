import math
def masofa(A, B):
    x1, y1 = A
    x2, y2 = B
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return d

x1, y1 = map(float, input("A nuqtasining koordinatalarini kiriting (x1, y1): ").split())
x2, y2 = map(float, input("B nuqtasining koordinatalarini kiriting (x2, y2): ").split())

A = (x1, y1)
B = (x2, y2)

distance = masofa(A, B)
print("A va B nuqtalari orasidagi masofa:", distance)

import math
def radiusni_topish(S):
    R = math.sqrt(S / math.pi)
    return R

S = float(input("Doiraning yuzini kiriting: "))

R = radiusni_topish(S)

print("Doira radiusi:", R)

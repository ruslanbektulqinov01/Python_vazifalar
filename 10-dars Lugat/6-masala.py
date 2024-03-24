def lugat_hosil_qil(n):

    lugat = {}
    for i in range(1, n + 1):
        lugat[i] = i ** 2
    return lugat

n = int(input("n ni kiriting: "))

print("Hosil qilingan lug'at:", lugat_hosil_qil(n))

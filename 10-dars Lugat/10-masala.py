s = "assalom"

d = {}
for harf in s:
    if harf in d:
        d[harf] += 1
    else:
        d[harf] = 1

print("Yaratilgan lug'at:", d)

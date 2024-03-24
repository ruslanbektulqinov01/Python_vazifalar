
lugat = {'c': 3, 'a': 1, 'b': 2}

lugat_saralangan = sorted(lugat.items(), key=lambda x: x[1])

print("Lug'atni qiymatlari bo'yicha saralangan:")
for item in lugat_saralangan:
    print(item)

# Lug'atni kalitlar bo'yicha saralash

lugat = {'c': 3, 'a': 1, 'b': 2}

lugat_saralangan = sorted(lugat.items(), key=lambda x: x[0])

print("Lug'atni kalitlar bo'yicha saralangan:")
for item in lugat_saralangan:
    print(item)

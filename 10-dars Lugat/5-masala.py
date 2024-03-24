def lugatda_mavjudmi(lugat, qiymat):

    if qiymat in lugat.values():
        return True
    else:
        return False


lugat1 = {'a': 1, 'b': 2, 'c': 3}
lugat2 = {'d': 4, 'e': 5, 'f': 6}

qiymat1 = 3
qiymat2 = 7

print(f"{qiymat1} lug'atda mavjudmi: {lugatda_mavjudmi(lugat1, qiymat1)}")
print(f"{qiymat2} lug'atda mavjudmi: {lugatda_mavjudmi(lugat1, qiymat2)}")
print(f"{qiymat1} lug'atda mavjudmi: {lugatda_mavjudmi(lugat2, qiymat1)}")
print(f"{qiymat2} lug'atda mavjudmi: {lugatda_mavjudmi(lugat2, qiymat2)}")

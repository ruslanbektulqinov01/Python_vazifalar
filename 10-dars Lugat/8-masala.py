def qiymat_ochir(lugat, kalit):

    if kalit in lugat:
        del lugat[kalit]
        print(f"'{kalit}' kaliti o'chirildi.")
    else:
        print(f"'{kalit}' kaliti lug'atda mavjud emas.")



lugat = {'a': 10, 'b': 20, 'c': 30}

kalit = input("O'chiriladigan qiymatning kalitini kiriting: ")
qiymat_ochir(lugat, kalit)

print("Yangilangan lug'at:", lugat)

n = 5
massiv = [2, 3, 4, 5, 6]
juft_sonlar = [x for x in massiv if x % 2 == 0]
miqdori = len(juft_sonlar)
print(miqdori)
print(*juft_sonlar)

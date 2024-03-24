n = 6
massiv = [7, 4, 7, 3, 5, 10]

juft_indeksla = [i+1 for i, x in enumerate(massiv) if x % 2 == 0]
toq_indeksla = [i+1 for i, x in enumerate(massiv) if x % 2 != 0]

print(*juft_indeksla)
print(*reversed(toq_indeksla))
print(*massiv)
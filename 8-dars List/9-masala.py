n = 5
massiv = [3, 2, 12, 7, 6]

toq_sonlar = [x for x in massiv if x % 2 != 0]
sorted_toq_sonlar = sorted(toq_sonlar)

print(len(sorted_toq_sonlar))
print(*sorted_toq_sonlar)

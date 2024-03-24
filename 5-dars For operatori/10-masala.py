n = int(input("n sonini kiriting: "))

yigindisi = sum((i + n) ** 3 for i in range(n, 2 * n + 1))

print(f"Yig'indi: {yigindisi}")
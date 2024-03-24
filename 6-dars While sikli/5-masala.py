n = int(input("n sonini kiriting (musbat butun son): "))

if n > 0 and (n & (n - 1)) == 0:
    k = 0
    while n > 1:
        n //= 2
        k += 1

    print(f"Darajaning ko'rsatkichi k: {k}")
else:
    print("N soni 2 ning biror bir darajasi emas!")

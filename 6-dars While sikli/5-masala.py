n = int(input("Enter n (positive integer): "))

if n > 0 and (n & (n - 1)) == 0:
    k = 0
    while n > 1:
        n //= 2
        k += 1

    print(f"The exponent of the power of 2 is k: {k}")
else:
    print("The number n is not a power of 2!")

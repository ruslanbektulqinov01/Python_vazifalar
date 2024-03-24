n = int(input("Enter n (positive integer): "))

k = 1
while k * k <= n:
    k += 1

k -= 1

print(f"The largest integer k whose square is less than or equal to n: {k}")

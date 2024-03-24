n = int(input("Enter n (positive integer greater than 1): "))

k = 1
while k ** 3 <= n:
    k += 1

k -= 1

print(f"The largest integer k such that k^3 <= n: {k}")

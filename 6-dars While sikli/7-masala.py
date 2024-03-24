n = int(input("Enter n (integer greater than or equal to 0): "))

k = 1
while k ** 2 <= n:
    k += 1

print(f"The smallest integer k whose square is greater than or equal to n: {k}")

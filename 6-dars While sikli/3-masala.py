n = int(input("Enter n (positive integer): "))
k = int(input("Enter k (positive integer): "))

quotient = 0
remainder = n

while remainder >= k:
    quotient += 1
    remainder -= k

print(f"The quotient of division: {quotient}, and the remainder: {remainder}")

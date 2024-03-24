a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

sum_of_squares = sum(x ** 2 for x in range(a, b + 1))

print(f"The sum of squares of numbers from {a} to {b} is: {sum_of_squares}")

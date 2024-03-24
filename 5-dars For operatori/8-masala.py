a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

product = 1

for number in range(a, b + 1):
    product *= number

print(f"The product is equal to {product}")

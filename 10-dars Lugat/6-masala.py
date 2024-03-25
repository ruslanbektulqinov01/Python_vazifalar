def generate_square_dict(n):
    dictionary = {}
    for i in range(1, n + 1):
        dictionary[i] = i ** 2
    return dictionary


n = int(input("Enter a value for n: "))

print("Generated square dictionary:", generate_square_dict(n))

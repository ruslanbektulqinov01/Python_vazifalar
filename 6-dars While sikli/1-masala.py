a = int(input("Enter a (positive number): "))
b = int(input("Enter b (positive number, greater than a): "))

segments_placed = 0
remaining_length = a

while remaining_length >= b:
    segments_placed += 1
    remaining_length -= b

print(f"Segments placed: {segments_placed}")
print(f"Remaining length: {remaining_length}")

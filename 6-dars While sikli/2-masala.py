a = int(input("Enter the value of a (positive number): "))
b = int(input("Enter the value of b (positive number, greater than a): "))

segments_placed = 0
remaining_length = a

while remaining_length >= b:
    segments_placed += 1
    remaining_length -= b

print(f"When placing segments of length {b} into a segment of length {a}, the number of segments placed is: {segments_placed}")

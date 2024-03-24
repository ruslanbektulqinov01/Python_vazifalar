n = int(input("Enter n (positive integer): "))

is_perfect_cube = False
if n > 0:
    cube_root = 1
    while cube_root**3 <= n:
        if cube_root**3 == n:
            is_perfect_cube = True
            break
        cube_root += 1

if is_perfect_cube:
    print("True")
else:
    print("False")

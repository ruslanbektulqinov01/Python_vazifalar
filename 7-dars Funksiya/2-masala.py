def RootsCount(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        return 2
    elif discriminant == 0:
        return 1
    else:
        return 0


coefficients = [(1, -5, 6), (1, -4, 4), (1, 4, 6)]

for coef in coefficients:
    a, b, c = coef
    roots_count = RootsCount(a, b, c)
    print(coef)
    print(roots_count)
    print()

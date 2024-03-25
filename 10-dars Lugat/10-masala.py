s = "universitet"

d = {}
for char in s:
    if char in d:
        d[char] += 1
    else:
        d[char] = 1

print("Created dictionary:", d)

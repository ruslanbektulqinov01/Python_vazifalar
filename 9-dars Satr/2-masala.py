def new_string(n1, n2, s1, s2):
    new_s = s1[:n1] + s2[-n2:]
    return new_s


n1 = 3
n2 = 2
s1 = "salom"
s2 = "dunyo"
new_s = new_string(n1, n2, s1, s2)
print(new_s)

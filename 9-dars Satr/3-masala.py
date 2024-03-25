def duplicate_chars(s, c):
    new_s = ''
    for char in s:
        new_s += char + c * 2
    return new_s

def insert_string(s, c, s0):
    index = s.find(c)
    if index != -1:
        new_s = s[:index] + s0 + s[index:]
    else:
        new_s = s + s0
    return new_s

s = "SALOM DUNYO"
c = 'A'
s0 = "XAYR HAMMAGA"

new_s1 = duplicate_chars(s, c)
print(new_s1)

new_s2 = insert_string(s, c, s0)
print(new_s2)

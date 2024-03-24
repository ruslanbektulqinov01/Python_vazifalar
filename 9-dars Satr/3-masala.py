def ikkilantirish(s, c):
   yangi_s = ''
   for char in s:
       yangi_s += char + c * 2
   return yangi_s

def joylashtirish(s, c, s0):
   index = s.find(c)
   if index != -1:
       yangi_s = s[:index] + s0 + s[index:]
   else:
       yangi_s = s + s0
   return yangi_s

s = "YAXWMSZ"
c = 'A'
s0 = "SZGA ETVOMMA"
yangi_s1 = ikkilantirish(s, c)
print(yangi_s1)

yangi_s2 = joylashtirish(s, c, s0)
print(yangi_s2)

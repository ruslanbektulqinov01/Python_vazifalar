def joylashtirish(s, c, s0):
   yangi_s = s.replace(c, s0 + c)
   return yangi_s

s = "QARAVORIN"
c = 'O'
s0 = "BRAT"
yangi_s = joylashtirish(s, c, s0)
print(yangi_s)


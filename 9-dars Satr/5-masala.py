def joylashtirish(s, c, s0):
   yangi_s = s.replace(c, c + s0)
   return yangi_s

s = "NMA GAP"
c = 'A'
s0 = "BOPTI"
yangi_s = joylashtirish(s, c, s0)
print(yangi_s)
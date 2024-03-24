def yengi_satr(n1, n2, s1, s2):
   yengi_s = s1[:n1] + s2[-n2:]
   return yengi_s

n1 = 3
n2 = 2
s1 = "salom"
s2 = "dunyo"
yengi_s = yengi_satr(n1, n2, s1, s2)
print(yengi_s)
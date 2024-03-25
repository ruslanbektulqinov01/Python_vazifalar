def insert_and_replace(s, c, s0):
   new_s = s.replace(c, s0 + c)
   return new_s


s = "UNIVERSITET"
c = 'I'
s0 = "PDP"

new_s = insert_and_replace(s, c, s0)
print(new_s)


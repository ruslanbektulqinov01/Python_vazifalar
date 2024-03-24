def RingS(r1, r2):
outer_area = math.pi * (r1**2)
   inner_area = math.pi * (r2**2)
   return outer_area - inner_area
radius_pairs = [(4, 2), (2, 1), (3, 2)]

for r1, r2 in radius_pairs:
   ring_area = RingS(r1, r2)
   print(r2)
   print(r1)
   print(ring_area)
   print()

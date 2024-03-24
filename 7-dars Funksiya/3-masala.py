import math

def CircleS(r):
   return math.pi * (r**2)
radius_list = [10, 100, 1]
for r in radius_list:
   circle_area = CircleS(r)
   print(r)
   print(circle_area)
   print()

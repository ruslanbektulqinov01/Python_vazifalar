def Quarter(x, y):
   if x > 0 and y > 0:
       return 1
   elif x < 0 and y > 0:
       return 2
   elif x < 0 and y < 0:
       return 3
   elif x > 0 and y < 0:
       return 4
   else:
     return 0
points = [(2, 3), (-2, 3), (2, -3)]
for point in points:
   x, y = point
  quarter = Quarter(x, y)
  if quarter != 0:
       print(f"Nuqta ({x}, {y}) {quarter}-choreda joylashgan")
  else:
      print(f"Nuqta ({x}, {y}) tekislida joylashmagan")
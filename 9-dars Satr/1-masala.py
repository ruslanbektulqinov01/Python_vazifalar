def edit_string(n, s):
   if len(s) > n:
       edited_string = s[:- (len(s) - n)]
   elif len(s) < n:
       edited_string = s + '.' * (n - len(s))
   else:
       edited_string = s
   return edited_string
n = 10
s = "NMA GAP"
edited_result = edit_string(n, s)
print(edited_result)

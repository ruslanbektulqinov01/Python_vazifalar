n = 5
a = 3
b = 4
masiv = [a, b]

for i in range(2, n):
   masiv.append(masiv[i-1] + masiv[i-2])

print(masiv)

n = 5
b = 2
q = 3
masiv = []
current_term = b
for i in range(n):
    masiv.append(current_term)
    current_term *= q
print(masiv)

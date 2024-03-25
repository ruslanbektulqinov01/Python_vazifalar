n = 10
masiv = [1, 1]
for i in range(2, n):
    masiv.append(masiv[-1] + masiv[-2])
print(masiv)

dictionary = {'c': 3, 'a': 1, 'b': 2}

sorted_dict = sorted(dictionary.items(), key=lambda x: x[0])

print("Dictionary sorted by keys:")
print(dict(sorted_dict))


dictionary = {'c': 3, 'a': 1, 'b': 2}

sorted_dict = dict(sorted(dictionary.items(), key=lambda x: x[1]))

print(f"Dictionary sorted: {sorted_dict}")

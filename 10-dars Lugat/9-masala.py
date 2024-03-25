def is_dict_empty(dictionary):
    if dictionary:
        return False
    else:
        return True

dict1 = {}
dict2 = {'a': 1, 'b': 2, 'c': 3}

print("dict1 is empty:", is_dict_empty(dict1))
print("dict2 is empty:", is_dict_empty(dict2))

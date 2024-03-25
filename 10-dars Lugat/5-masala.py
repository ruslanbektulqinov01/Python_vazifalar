def is_value_in_dict(dictionary, value):
    if value in dictionary.values():
        return True
    else:
        return False

dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'d': 4, 'e': 5, 'f': 6}

value1 = 3
value2 = 7

print(f"{value1} is in dict1: {is_value_in_dict(dict1, value1)}")
print(f"{value2} is in dict1: {is_value_in_dict(dict1, value2)}")
print(f"{value1} is in dict2: {is_value_in_dict(dict2, value1)}")
print(f"{value2} is in dict2: {is_value_in_dict(dict2, value2)}")

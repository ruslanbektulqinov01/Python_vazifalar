def remove_key(dictionary, key):
    if key in dictionary:
        del dictionary[key]
        print(f"The key '{key}' is deleted.")
    else:
        print(f"The key '{key}' does not exist in the dictionary.")


dictionary = {'a': 10, 'b': 20, 'c': 30}

key_to_remove = input("Enter the key to be removed: ")
remove_key(dictionary, key_to_remove)

print("Updated dictionary:", dictionary)

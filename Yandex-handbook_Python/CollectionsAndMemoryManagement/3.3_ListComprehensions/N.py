data = {'a': [1, 2, 3], 'b': [5, 2, 5], 'c': [7, 15, 3]}
print(set(key for key, value in data.items() if sorted(set(value)) != sorted(value)))
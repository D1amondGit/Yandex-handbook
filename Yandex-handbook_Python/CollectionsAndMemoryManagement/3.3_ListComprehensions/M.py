data = {'a': [100], 'b': [20, 5], 'c': [7, 15, 3]}
print(''.join(sorted([key for key, value in data.items() if sum(value) == min([sum(value) for value in data.values()])])[0]))
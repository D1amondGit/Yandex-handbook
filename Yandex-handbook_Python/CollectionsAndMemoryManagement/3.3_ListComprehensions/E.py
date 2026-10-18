numbers = [number for number in range(16, 100, 4)]
print(set([i**2 for i in range(max(numbers)) if i**2 in numbers]))
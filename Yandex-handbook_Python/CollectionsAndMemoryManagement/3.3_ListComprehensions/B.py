a = 5
b = -4
print([i**2 for i in range(a, b + 1 if a < b else b - 1, 1 if a < b else -1)])
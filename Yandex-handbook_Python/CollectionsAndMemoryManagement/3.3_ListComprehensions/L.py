numbers = {2, 4, 5, 7, -10, -8, 10, -9, -1}
print(max([i * j for i in numbers for j in numbers if i != j]))
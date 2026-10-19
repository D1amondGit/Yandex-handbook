numbers = set(range(11, 50, 2))
print(set([i for i in numbers if sum(1 for j in range(1, i + 1) if i % j == 0) == 2]))
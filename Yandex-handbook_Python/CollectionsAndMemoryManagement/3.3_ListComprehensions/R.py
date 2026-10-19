numbers = {15, 49, 36}
print({i: [j for j in range(1, i + 1) if i % j == 0] for i in sorted(numbers)})
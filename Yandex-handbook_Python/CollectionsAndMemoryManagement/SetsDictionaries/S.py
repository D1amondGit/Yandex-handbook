toys = dict()
n = int(input())
for i in range(n):
    s = input()
    name = s.split(":")[0].strip()
    items = s.split(":")[1].strip().split(", ")
    for toy in items:
        toys.setdefault(toy, set()).add(name)
unique_toys = []
for toy, names in toys.items():
    if len(names) == 1:
        unique_toys.append(toy)
unique_toys.sort()
for toy in unique_toys:
    print(toy)
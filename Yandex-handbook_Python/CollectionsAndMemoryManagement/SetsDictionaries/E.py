n = int(input())
m = int(input())
allKids = set()
removedKids = set()
for i in range(n + m):
    s = input()
    if s in allKids:
        removedKids.add(s)
    allKids.add(s)
un = len(allKids - removedKids)
print(un if un > 0 else "Таких нет")
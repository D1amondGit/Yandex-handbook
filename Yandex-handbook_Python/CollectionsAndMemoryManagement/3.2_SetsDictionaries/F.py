n = int(input())
m = int(input())
allKids = set()
removedKids = set()
for i in range(n + m):
    s = input()
    if s in allKids:
        removedKids.add(s)
    allKids.add(s)
un = allKids - removedKids
if len(un) == 0:
    print("Таких нет")
else:
    for i in sorted(list(un)):
        print(i)
n = int(input())
m = int(input())
loveMan = set()
loveOvs = set()
for i in range(n):
    loveMan.add(input())
for i in range(m):
    loveOvs.add(input())
un = len(loveOvs & loveMan)
print(un if un > 0 else "Таких нет")
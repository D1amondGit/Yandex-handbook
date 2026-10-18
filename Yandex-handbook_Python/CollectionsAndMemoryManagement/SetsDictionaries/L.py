n = int(input())
fams = dict()
for i in range(n):
    s = input()
    if s in fams:
        fams[s] += 1
    else:
        fams[s] = 1
count = 0
isFam = False
for key, value in sorted(fams.items()):
    if value > 1:
        print(f"{key} - {value}")
        isFam = True
if not isFam:
    print("Однофамильцев нет")
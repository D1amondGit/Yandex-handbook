n = int(input())
fams = dict()
for i in range(n):
    s = input()
    if s in fams:
        fams[s] += 1
    else:
        fams[s] = 1
count = 0
for value in fams.values():
    if value > 1:
        count += value
print(count)
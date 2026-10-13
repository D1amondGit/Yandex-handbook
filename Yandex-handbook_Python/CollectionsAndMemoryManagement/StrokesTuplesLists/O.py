n = list(map(int, input().split()))
nod = n[0]
for m in n:
    while m:
        nod, m = m, nod % m
    nod = nod + m
print(nod)

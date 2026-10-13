n = int(input())
nod = int(input())
for i in range(n - 1):
    m = int(input())
    while m:
        nod, m = m, nod % m
    nod = nod + m
print(nod)
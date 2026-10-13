n = int(input())
m = int(input())
if n > m:
    k = -1
    m -= 2
else:
    k = 1
for i in range(n, m + 1, k):
    print(i, end=" ")
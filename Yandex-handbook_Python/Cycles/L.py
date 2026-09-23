n = 0
k = int(input())
while (k > 0):
    n = max(k % 10, n)
    k //= 10
print(n)
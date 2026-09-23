n = int(input())
if n == 1:
    print("NO")
    exit()
k = False
for i in range(2, int(n**0.5) + 1):
    if n % i == 0 and i != n:
        k = True
if k:
    print("NO")
else:
    print("YES")
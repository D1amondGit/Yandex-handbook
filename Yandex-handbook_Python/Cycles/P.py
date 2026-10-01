n = int(input())
n1 = n
m = 0
while n1 > 0:
    m = m * 10 + n1 % 10
    n1 //= 10
if (n == m):
    print("YES")
else:
    print("NO")
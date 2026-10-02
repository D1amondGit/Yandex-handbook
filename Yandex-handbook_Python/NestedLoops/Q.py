count = 0
k = int(input())
for i in range(k):
    n = int(input())
    n1 = n
    m = 0
    while n1 > 0:
        m = m * 10 + n1 % 10
        n1 //= 10
    if n == m:
        count += 1
print(count)
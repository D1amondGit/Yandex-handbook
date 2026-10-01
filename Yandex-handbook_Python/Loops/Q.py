
n = int(input())
n1 = n
m = 0
d = 1
while n1 > 0:
    if n1 % 2 != 0:
        m = m + d * (n1 % 10)
        d *= 10
    else:
        pass
    n1 //= 10
print(m)
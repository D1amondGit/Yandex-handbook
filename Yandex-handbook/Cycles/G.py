n = int(input())
m = int(input())
n1 = n
m1 = m
while m1:
    n1, m1 = m1, n1 % m1
gcd = n1 + m1
print(int(n * m / gcd))
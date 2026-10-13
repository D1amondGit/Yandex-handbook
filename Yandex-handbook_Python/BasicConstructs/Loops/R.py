n = int(input())
n1 = n
s = ""
d = 2
while d <= n:
    if n1 % d == 0:
        s += f"{d} * "
        n1 //= d
    else:
        d += 1

print(s[:-3])
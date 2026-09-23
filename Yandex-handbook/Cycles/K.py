n = 0
k = int(input())


while k > 0:
    n += k % 10
    k //= 10
print(n)
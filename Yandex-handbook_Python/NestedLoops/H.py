name = ""
n = int(input())
maxsum = 0
for i in range(n):
    thisSum = 0
    thisName = input()
    k = int(input())
    while k > 0:
        thisSum += k % 10
        k //= 10

    if thisSum >= maxsum:
        maxsum = thisSum
        name = thisName
print(name)
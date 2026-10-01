n = int(input())
number = 0
for i in range(n):
    maxnumber = 0
    k = int(input())
    while (k > 0):
        maxnumber = max(k % 10, maxnumber)
        k //= 10
    number = number * 10 + maxnumber
print(number)
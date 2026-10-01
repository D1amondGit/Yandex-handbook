n = 0
numbers = int(input())
for i in range(numbers):
    k = int(input())
    while k > 0:
        n += k % 10
        k //= 10
print(n)
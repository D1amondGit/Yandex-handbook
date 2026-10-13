count = 0
nums = int(input())
for i in range(nums):
    n = int(input())
    if n == 1:
        continue
    k = False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0 and i != n:
            k = True
    if not k:
        count += 1
print(count)
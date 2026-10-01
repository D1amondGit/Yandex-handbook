n = int(input())
m = int(input())
i = 1

max_number = m * n
width = 0
while max_number:
    width += 1
    max_number //= 10

while i <= n:
    for k in range(1, m + 1):
        if i % 2 != 0:
            number = k + (i - 1) * m
        else:
            number = i * m - k + 1
        print(f"{number:>{width}}", end=" ")
        number = number + n
    i += 1
    print("")

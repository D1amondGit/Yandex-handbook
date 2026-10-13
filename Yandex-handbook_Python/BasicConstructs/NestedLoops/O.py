n = int(input())
m = int(input())
i = 0

max_number = m * n
width = 0
while max_number:
    width += 1
    max_number //= 10

while i < n: #номер строки
    number = i
    for k in range(m): #номер столбца
        if k % 2 == 0:
            number = k * n + i + 1
        else:
            number = k * n + n - i
        print(f"{number:>{width}}", end=" ")
    i += 1
    print("")

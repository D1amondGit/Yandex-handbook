n = int(input())
m = int(input())
i = 1
max_number = m * n
width = 0
while max_number:
    width += 1
    max_number //= 10

while i <= n * m: #номер строки
    for k in range(m): #номер столбца
        if i <= n * m:
            print(f'{i:>{width}}',end=' ')
            i += 1
    print("")

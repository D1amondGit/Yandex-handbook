n = int(input())
m = int(input())
i = 1

max_number = m * n
width = 0
while max_number:
    width += 1
    max_number //= 10

while i <= n: #номер строки
    number = i
    for k in range(m): #номер столбца
        print(f"{number:>{width}}",end=" ")
        number = number + n
    i += 1
    print("")

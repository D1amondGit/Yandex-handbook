n = int(input())
k = 1
i = 1
while i <= n:
    for j in range(1, k + 1):
        if i <= n:
            print(i, end=" ")
            i += 1
    print("")
    k += 1
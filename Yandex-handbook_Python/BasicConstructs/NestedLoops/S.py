n = int(input())

width_column = len(str(n // 2)) if n % 2 == 0 else len(str(n // 2 + 1))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        vlogx = min(j, n - j + 1)
        vlogy = min(i, n - i + 1)
        print(f"{min(vlogx, vlogy):>{width_column}}", end=" ")
    print("")

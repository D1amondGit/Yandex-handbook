n = int(input())
k = 1
i = 1

while i <= n:
    lenstroke = 0
    for j in range(1, k + 1):
        if i <= n:
            lenstroke += len(f"{i} ") if j < k and i < n else len(f"{i}")
            i += 1
    k += 1

i = 1
k = 1
while i <= n:
    s = ""
    for j in range(1, k + 1):
        if i <= n:
            s += f"{i} " if j < k and i < n else f"{i}"
            i += 1
    print(f"{s:^{lenstroke}}")
    k += 1


n = int(input())
width = int(input())

for i in range(1, n + 1):
    lenstroke = 0
    for j in range(1, n + 1):

        print(s:= f"{i * j:^{width}}", end="")
        if j < n:
            print("|", end="")
            lenstroke += 1
        lenstroke += len(s)
    if i < n:
        print(f"\n{'-' * lenstroke}")
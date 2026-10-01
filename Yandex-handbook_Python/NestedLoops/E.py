n = int(input())
k = 0
for i in range(n):
    rabbit = False
    while (s := input()) != "ВСЁ":
        if "зайка" in s:
            rabbit = True
    if rabbit:
        k += 1
print(k)
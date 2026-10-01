n = 500
vg = 1001
ng = 1
print(n)
while (s := input()) != "Угадал!":
    if s == "Меньше":
        vg = n
    elif s == "Больше":
        ng = n
    else:
        pass
    n = (vg + ng) // 2
    print(n)
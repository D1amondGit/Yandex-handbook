n = int(input())
k = 0
for i in range(n):
    if "зайка" in (stroke := input()):
        k += 1
print(k)
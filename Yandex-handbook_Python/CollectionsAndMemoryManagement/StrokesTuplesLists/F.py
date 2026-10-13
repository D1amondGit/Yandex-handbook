n = int(input())
count = 0
for i in range(n):
    count += (s := input()).count("зайка")
print(count)
n = int(input())
s = "YES"
for i in range(n):
    if input()[0] not in "абв":
        s = "NO"
print(s)
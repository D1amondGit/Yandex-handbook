n = int(input())
for i in range(n):
    count = (s := input()).find("зайка")
    print(count + 1) if count != -1 else print("Заек нет =(")
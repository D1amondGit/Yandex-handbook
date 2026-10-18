n = int(input())
products = set()
for i in range(n):
    products.add(input())
m = int(input())
flag = False
dishes = []
for i in range(m):
    dishName = input()
    countP = int(input())
    dishRecept = set()
    for k in range(countP):
        dishRecept.add(input())
    if dishRecept <= products:
        dishes.append(dishName)
        flag = True
dishes.sort()
for i in dishes:
    print(i)
if not flag:
    print("Готовить нечего")
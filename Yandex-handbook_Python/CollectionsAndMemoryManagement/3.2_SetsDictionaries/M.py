n = int(input())
dishes = set()
for i in range(n):
    dishes.add(input())

m = int(input())
week_dishes = set()
for i in range(m):
    n_1 = int(input())
    for k in range(n_1):
        week_dishes.add(input())
itog_dishes = dishes - week_dishes
if len(itog_dishes) > 0:
    for i in sorted(itog_dishes):
        print(i)
else:
    print("Готовить нечего")
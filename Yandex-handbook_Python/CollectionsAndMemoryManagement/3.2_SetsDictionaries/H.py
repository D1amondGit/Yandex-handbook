families = dict()
n = int(input())

for i in range(n):
    stroke = input().split()
    last_name, foods = stroke[0], stroke[1:]
    for food in foods:
        if food in families:
            families[food].append(last_name)
        else:
            families[food] = [last_name]
foodd = input()
if foodd in families:
    for fam in sorted(families[foodd]):
        print(fam)
else:
    print("Таких нет")
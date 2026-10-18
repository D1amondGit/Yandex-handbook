viewObjects = set()
while (s := input()) != "":
    sMassive = s.split()
    for i in range(len(sMassive)):
        if i == 0:
            if sMassive[i + 1] == "зайка":
                viewObjects.add(sMassive[i])
        elif i == len(sMassive) - 1:
            if sMassive[i - 1] == "зайка":
                viewObjects.add(sMassive[i])
        elif "зайка" in [sMassive[i + 1], sMassive[i - 1]]:
            viewObjects.add(sMassive[i])
for i in viewObjects:
    print(i)
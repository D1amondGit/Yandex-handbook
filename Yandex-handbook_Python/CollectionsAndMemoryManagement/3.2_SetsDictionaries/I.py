objects = dict()
while (s := input()) != "":
    for obb in s.split():
        if obb in objects:
            objects[obb] += 1
        else:
            objects[obb] = 1
for key, value in objects.items():
    print(key, value)

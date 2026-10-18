friends_1_tier = dict()
names = set()
while (s := input()) != "":
    name1, name2 = s.split()
    if name1 not in friends_1_tier:
        friends_1_tier[name1] = set()
    if name2 not in friends_1_tier:
        friends_1_tier[name2] = set()
    names.update({name1, name2})

    friends_1_tier[name1].add(name2)
    friends_1_tier[name2].add(name1)

friends_2_tier = dict()
for name, friendsSet in friends_1_tier.items():
    allFriendsSet = set()
    for friend in friendsSet:
        allFriendsSet.update(friends_1_tier[friend])
    friends_2_tier[name] = allFriendsSet - friendsSet - {name}
for name in sorted(names):
    print(f"{name}: {', '.join(sorted(friends_2_tier[name]))}")
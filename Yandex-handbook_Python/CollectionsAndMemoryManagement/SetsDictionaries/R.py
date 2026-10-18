n = int(input())
possible_points = dict()
for i in range(n):
    x, y = map(int, input().split())
    point_box = (x // 10, y // 10)
    possible_points.setdefault(str(point_box), set()).add((x,y))
max_count = 0
for points in possible_points:
    max_count = max(max_count, len(possible_points[points]))
print(max_count)
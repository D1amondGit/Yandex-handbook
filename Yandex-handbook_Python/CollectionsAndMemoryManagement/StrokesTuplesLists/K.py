n = int(input())
strokes = []
for i in range(n):
    strokes.append(input())
find = input()
findStrokes = []
for title in strokes:
    if find.lower() in title.lower():
        findStrokes.append(title)
for k in findStrokes:
    print(k)

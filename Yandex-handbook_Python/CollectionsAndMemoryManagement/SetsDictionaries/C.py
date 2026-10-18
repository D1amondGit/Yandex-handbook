n = int(input())
words = set()
for i in range(n):
    stroke = input()
    for word in stroke.split():
        words.add(word)
for word in words:
    print(word)
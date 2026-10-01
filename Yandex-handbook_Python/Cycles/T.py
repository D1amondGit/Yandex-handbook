n = int(input())
hprev = 0

for i in range(n):
    correct = False
    b = int(input())
    h = b % 256
    if h < 100:
        r = ((b - h) // 256) % 256
        m = (b - h - r * 256) // 256**2
        if h == (37 * (m + r + hprev)) % 256:
            correct = True
            hprev = h
    if not correct:
        print(i)
        exit()
print(-1)

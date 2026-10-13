s = input()
m = []
for i in s.split():
    if i in "*+-":
        b = m.pop()
        a = m.pop()
        m.append(eval(f"{a} {i} {b}"))
    else:
        m.append(int(i))
print(m[0])
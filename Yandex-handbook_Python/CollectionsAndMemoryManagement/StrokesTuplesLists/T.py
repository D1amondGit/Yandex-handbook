import math

s = input()
m = []
for i in s.split():
    if i in "*+-/":
        b = m.pop()
        a = m.pop()
        if i == "*":
            m.append(a * b)
        if i == "+":
            m.append(a + b)
        if i == "-":
            m.append(a - b)
        if i == "/":
            m.append(a // b)
    elif i in "~!#":
        a = m.pop()
        if i == "~":
            m.append(-a)
        if i == "!":
            m.append(math.factorial(a))
        if i == "#":
            m.append(a)
            m.append(a)
    elif i == "@":
        a = m.pop()
        b = m.pop()
        c = m.pop()
        m.append(b)
        m.append(a)
        m.append(c)
    else:
        m.append(int(i))
print(m[0])
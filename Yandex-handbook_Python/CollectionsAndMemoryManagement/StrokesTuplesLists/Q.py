s = input()
new_s = ""
for char in s:
    if char != " ":
        new_s += char.lower()
print("YES") if new_s == new_s[::-1] else print("NO")
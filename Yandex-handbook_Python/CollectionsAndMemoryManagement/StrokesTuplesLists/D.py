while (s := input()) != "":
    if s[:2] == "##":
        s = s[2:]
    if s[-3:] == "@@@":
        continue
    print(s)

while (s := input()) != "":
    if s.startswith("#"):
        continue
    if (idx := s.find("#")) != -1:
        print(s[:idx].rstrip())
    else:
        print(s.rstrip())
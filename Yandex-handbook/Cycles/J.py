x = 0
y = 0

while ((s := input()) != "СТОП"):
    match s:
        case "СЕВЕР":
            y += int(input())
        case "ВОСТОК":
            x += int(input())
        case "ЮГ":
            y -= int(input())
        case "ЗАПАД":
            x -= int(input())
print(f"{y}\n{x}")
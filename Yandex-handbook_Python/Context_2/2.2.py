N, M, Q, cw, sw, hw, tw = map(int, input().split())
last_name = input()
rating = 0
if M > 0 and cw > 0 and sw > 0 and hw > 0 and tw > 0:
    for i in range(M):
        a, b, c, d = map(int, input().split(","))
        rating += a * cw + b * sw + c * hw + d * tw
    if rating > Q:
        print("Во введённых данных ошибка")
    else:
        percentRating = round(rating * 100 / Q)
        print(f"{last_name} {percentRating}%")
else:
    print("Во введённых данных ошибка")
N, M, Q, cw, sw, hw, tw = map(int, input().split())
max_rating = 0
min_rating = Q
sum_rating = 0

firstName = ""
secondName = ""
thirdName = ""
second_rating = 0
third_rating = 0
if M > 0 and N >= 3 and cw > 0 and sw > 0 and hw > 0 and tw > 0:
    for j in range(N):
        last_name = input()
        rating = 0
        for i in range(M):
            a, b, c, d = map(int, input().split(","))
            rating += a * cw + b * sw + c * hw + d * tw
        if rating > Q:
            print("Во введённых данных ошибка")
            exit()
        else:
            sum_rating += rating
            if rating > max_rating:
                third_rating = second_rating
                thirdName = secondName

                second_rating = max_rating
                secondName = firstName

                max_rating = rating
                firstName = last_name

            elif rating > second_rating:
                third_rating = second_rating
                thirdName = secondName

                second_rating = rating
                secondName = last_name

            elif rating > third_rating:
                third_rating = rating
                thirdName = last_name
            min_rating = min(min_rating, rating)

    avg_rating = round(sum_rating * 100 / Q / N)
    max_rating = round(max_rating * 100 / Q)
    min_rating = round(min_rating * 100 / Q)
    second_rating = round(second_rating * 100 / Q)
    third_rating = round(third_rating * 100 / Q)

    print(f"{max_rating} {avg_rating} {min_rating}")
    print(f"{firstName} {max_rating}%")
    print(f"{secondName} {second_rating}%")
    print(f"{thirdName} {third_rating}%")
    if avg_rating > 50:
        print("Курс усваивается хорошо")
    else:
        print("Курс усваивается плохо")
else:
    print("Во введённых данных ошибка")
    exit()
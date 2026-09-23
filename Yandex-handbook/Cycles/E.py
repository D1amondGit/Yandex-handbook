suma = 0;
while ((buy := float(input())) != 0):
    if buy >= 500:
        suma += buy * 0.9
    else:
        suma += buy
print(f"{suma:.1f}")
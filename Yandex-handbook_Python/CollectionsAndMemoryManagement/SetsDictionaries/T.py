from math import gcd
numbers = list(map(int, input().split("; ")))
numbers.sort()
numbers_gcd = dict()
for num in numbers:
    for num2 in numbers:
        if gcd(num, num2) == 1:
            numbers_gcd.setdefault(num, set()).add(num2)
for num, primeNums in numbers_gcd.items():
    print(f"{num} - {', '.join(map(str, sorted(primeNums)))}")

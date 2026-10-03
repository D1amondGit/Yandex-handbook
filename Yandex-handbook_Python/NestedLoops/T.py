n = int(input())
optimalsum = 0
systemOfNumeric = 10
for i in range(10, 1, -1):
    sumnums = 0
    n1 = n
    while n1:
        sumnums += n1 % i
        n1 //= i
    if optimalsum <= sumnums:
        optimalsum = sumnums
        systemOfNumeric = i
print(systemOfNumeric)
numbers = list(map(int, input().split()))
m = []
for i in range(len(numbers)):
    dictNum = dict()
    num = numbers[i]
    binNum = bin(num)
    strNum = str(binNum)[2:]
    dictNum["digits"] = len(strNum)
    dictNum["units"] = strNum.count("1")
    dictNum["zeros"] = strNum.count("0")
    m.append(dictNum)
print(m)
L = int(input())
N = int(input())
for i in range(N):
    s = input()
    s = s[:L - 3] + "..." if len(s) > L else s
    print(s)

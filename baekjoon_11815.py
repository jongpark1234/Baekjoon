n = int(input())
x = list(map(int, input().split()))
for i in range(n):
    print(1 if x[i] == int(x[i] ** 0.5) ** 2 else 0, end=' ')

n, m = map(int, input().split()); temp = 0
for i in range(n):
    for j in range(m - 1):
        temp += 1
        print(temp, end=' ')
    temp += 1
    print(temp)

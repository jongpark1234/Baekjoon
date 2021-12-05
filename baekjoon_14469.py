cows = sorted([list(map(int, input().split())) for _ in range(int(input()))], key = lambda x: x[0])
second = 0
for i in cows:
    if i[0] - second > 0:
        second += i[0] - second
    second += i[1]
print(second)

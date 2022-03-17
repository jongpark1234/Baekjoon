m, n, k = map(int, input().split())
signal = [input() for _ in range(m)]
for i in signal:
    enlarged = ''
    for j in i:
        enlarged += j * k
    print((enlarged + '\n') * k, end='')

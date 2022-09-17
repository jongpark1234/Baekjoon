def calc(num):
    if num == 0:
        return 0
    elif num not in grundy:
        numset = set()
        for i in range(m):
            if ((num >> (i << 1)) & 3) > 0:
                numset.add(calc(num - (1 << (i << 1))))
        for i in range(m - 1):
            if ((num >> (i << 1)) & 15) == 10:
                numset.add(calc(num - (10 << (i << 1))))
        temp = 0
        while temp in numset:
            temp += 1
        grundy[num] = temp
    return grundy[num]
grundy = {}
for _ in range(3):
    result = 0
    n, m = map(int, input().split())
    graph = [[]] + [[0] + list(map(lambda x: -1 if x == '#' else 0, input())) for _ in range(n)]
    if graph == [[], [0, 0]] or graph == [[], [0, -1, 0]]:
        print('Y')
        continue
    for i in range(1, (n + 1 >> 1) + 1):
        num = 0
        for j in range(1, m + 1):
            num = (num << 2) + sum(graph[(i << 1) - k][j] == 0 for k in range(2))
        result ^= calc(num)
    print('Y' if result else 'M')

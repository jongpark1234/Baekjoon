result = turn = 0
n = int(input())
cards = [sorted(list(map(int, input().split()))) for _ in range(2)]
while True:
    if not cards[turn] or cards[turn][-1] < cards[not turn][0]:
        break
    if cards[turn][0] > cards[not turn][-1]:
        result += len(cards[turn]) * [1, -1][turn]
        break
    numlist = []
    temp = len(cards[turn])
    best = [temp * [-1, 1][turn], temp * [1, -1][turn]]
    for i in range(len(cards[turn])):
        j = 0
        while j < temp and cards[turn][i] >= cards[not turn][j]:
            j += 1
        if j < temp:
            numlist.append((i, j))
    for i, j in numlist:
        if i - j > best[turn] - best[not turn]:
            best[turn] = i
            best[not turn] = j
    del cards[0][best[0]]
    del cards[1][best[1]]
    result += (temp - 1) * [1, -1][turn]
    turn = not turn
print(result)

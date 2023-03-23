def bfs(now):
    numlist = []
    if now in memoization:
        return memoization[now]
    if now % 3 == 0:
        numlist.append(bfs(now // 3))
    if now % 2 == 0:
        numlist.append(bfs(now // 2))
    if (now - 1) % 3 == 0 or (now - 1) % 2 == 0:
        numlist.append(bfs(now - 1))
    if (now - 2) % 3 == 0:
        numlist.append(bfs(now - 2) + 1)
    ret = min(numlist) + 1
    memoization[now] = ret
    return ret
memoization = { 1: 0, 2: 1, 3: 1 }
print(bfs(int(input())))

def solve(root):
    idx = temp = 0
    visited = [0] + [False for _ in range(n)]
    slack = [0] + [float('inf') for _ in range(n)]
    match[0] = root
    while True:
        visited[idx] = True
        x = match[idx]
        delta = float('inf')
        for i in range(n + 1):
            if not visited[i]:
                if xlist[x] + ylist[i] - cost[x][i] < slack[i]:
                    slack[i] = xlist[x] + ylist[i] - cost[x][i]
                    prev[i] = idx
                if slack[i] < delta:
                    delta = slack[i]
                    temp = i
        for i in range(n + 1):
            if visited[i]:
                xlist[match[i]] -= delta
                ylist[i] += delta
            else:
                slack[i] -= delta
        idx = temp
        if match[idx] == -1:
            break
    while True:
        temp = prev[idx]
        match[idx] = match[temp]
        idx = temp
        if not idx:
            break
def code(x):
    if 'A' <= x <= 'Z':
        return 2 ** (116 - ord(x))
    else:
        return 2 ** (122 - ord(x))
xlist = [0 for _ in range(55)]
ylist = [0 for _ in range(55)]
prev = [0 for _ in range(55)]
match = [0 for _ in range(55)]
cost = [[0 for _ in range(55)] for _ in range(55)]
message = [' ']
result = []
n = int(input())
for i in range(n):
    message.append(' ' + input())
for i in range(1, n + 1):
    for j in range(1, n + 1):
        cost[i][j] = code(message[i][j])
for i in range(1, n + 1):
    xlist[i] = ylist[i] = 0
    match[i] = -1
    for j in range(1, n + 1):
        xlist[i] = max(xlist[i], cost[i][j])
for i in range(1, n + 1):
    solve(i)
for i in range(1, n + 1):
    result.append(message[match[i]][i])
print(''.join(sorted(result)))

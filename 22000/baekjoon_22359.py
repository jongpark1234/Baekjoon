def coloring(a, b, w, c, dic):
    for j in range(b, b + w):
        for i in range(a, a + w):
            if dic == 0 and a + w // 2 <= i and b + w // 2 <= j:
                continue
            if dic == 1 and a + w // 2 > i and b + w // 2 <= j:
                continue
            if dic == 2 and a + w // 2 > i and b + w // 2 > j:
                continue
            if dic == 3 and a + w // 2 <= i and b + w // 2 > j:
                continue
            plate[j][i] = c
def dfs(a, b, w, dic):
    if w == 4:
        if dic == 0:
            coloring(a, b, w // 2, 'b', 0)
            coloring(a + w // 4, b + w // 4, w // 2, 'a', 0)
            coloring(a, b + w // 2, w // 2, 'c', 3)
            coloring(a + w // 2, b, w // 2, 'c', 1)
        elif dic == 1:
            coloring( a, b, w // 2, 'b', 0)
            coloring(a + w // 2, b, w // 2, 'c', 1)
            coloring(a + w // 4, b + w // 4, w // 2, 'a', 1)
            coloring(a + w // 2, b + w // 2, w // 2, 'b', 2)
        elif dic == 2:
            coloring(a + w // 4, b + w // 4, w // 2, 'a', 2)
            coloring(a + w // 2, b + w // 2, w // 2, 'b', 2)
            coloring(a + w // 2, b, w // 2, 'c', 1)
            coloring(a, b + w // 2, w // 2, 'c', 3)
        elif dic == 3:
            coloring(a, b, w // 2, 'b', 0)
            coloring(a + w // 2, b + w // 2, w // 2, 'b', 2)
            coloring(a + w // 4, b + w // 4, w // 2, 'a', 3)
            coloring(a, b + w // 2, w // 2, 'c', 3)
        return
    if dic == 0:
        dfs(a, b, w // 2, 0)
        dfs(a + w // 2, b, w // 2, 1)
        dfs(a, b + w // 2, w // 2, 3)
        dfs(a + w // 4, b + w // 4, w // 2, 0)
    elif dic == 1:
        dfs(a, b, w // 2, 0)
        dfs(a + w // 2, b, w // 2, 1)
        dfs(a + w // 4, b + w // 4, w // 2, 1)
        dfs(a + w // 2, b + w // 2, w // 2, 2)
    elif dic == 2:
        dfs(a + w // 2, b, w // 2, 1)
        dfs(a, b + w // 2, w // 2, 3)
        dfs(a + w // 2, b + w // 2, w // 2, 2)
        dfs(a + w // 4, b + w // 4, w // 2, 2)
    elif dic == 3:
        dfs(a, b, w // 2, 0)
        dfs(a, b + w // 2, w // 2, 3)
        dfs(a + w // 4, b + w // 4, w // 2, 3)
        dfs(a + w // 2, b + w // 2, w // 2, 2)
def dfs2(a, b, w):
    if w == 2:
        temp = a // 2 + b // 2
        nc = 'b' if ~temp & 1 else 'c'
        if x < a + w // 2 and y < b + w // 2:
            coloring(a, b, w, nc, 2)
        elif x < a + w // 2 and y >= b + w // 2:
            coloring(a, b, w, nc, 1)
        elif x >= a + w // 2 and y < b + w // 2:
            coloring(a, b, w, nc, 3)
        elif x >= a + w // 2 and y >= b + w // 2:
            coloring(a, b, w, nc, 0)
        return
    if x < a + w // 2 and y < b + w // 2:
        dfs(a, b, w, 2)
        dfs2(a, b, w // 2)
    elif x < a + w // 2 and y >= b + w // 2:
        dfs(a, b, w, 1)
        dfs2(a, b + w // 2, w // 2)
    elif x >= a + w // 2 and y < b + w // 2:
        dfs(a, b, w, 3)
        dfs2(a + w // 2, b, w // 2)
    elif x >= a + w // 2 and y >= b + w // 2:
        dfs(a, b, w, 0)
        dfs2(a + w // 2, b + w // 2, w // 2)
plate = [['X' for _ in range(2001)] for _ in range(2001)]
t, k = map(int, input().split())
for _ in range(t):
    y, x = map(lambda x: int(x) - 1, input().split())
    plate[y][x] = '@'
    dfs2(0, 0, 1 << k)
    for i in range(1 << k):
        for j in range(1 << k):
            print(plate[i][j], end='')
        print()

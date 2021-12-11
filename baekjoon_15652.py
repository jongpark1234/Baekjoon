n, m = map(int, input().split())
sequence = []
def dfs(depth, index, n, m):
    if depth == m:
        print(*sequence)
        return
    for i in range(index, n):
        sequence.append(i + 1)
        dfs(depth + 1, i, n, m)
        sequence.pop()
dfs(0, 0, n, m)

def solve(x):
    global m
    if x == 1:
        adj[m][m] = '1'
        m += 1
        return
    if x & 1:
        solve(x - 1)
        adj[m - 1][m] = '1'
        adj[m][m] = '1'
        adj[m][0] = '1'
        m += 1
        return
    else:
        solve(x // 2)
        adj[m - 1][m] = '1'
        adj[m][m] = adj[m][m + 1] = adj[m + 1][m] = adj[m + 1][m + 1] = '1'
        m += 2
        return
for _ in range(int(input())):
    n, m = int(input()), 0
    adj = [['0' for _ in range(100)] for _ in range(100)]
    solve(n)
    print(m)
    for i in range(m):
        print(''.join(adj[i][:m]))

def search(x, y, z, v):
    visited[x][y][z] = True
    result.add(v[-1])
    for i in range(6):
        nx, ny, nz, nv = x + dx[i], y + dy[i], z + dz[i], v[:]
        if not ((0 <= nx < h and 0 <= ny < n and 0 <= nz < m) and (graph[nx][ny][nz] == 'x' and not visited[nx][ny][nz])):
            continue
        nv[i >> 1], nv[-1] = nv[-1], nv[i >> 1]
        nv[-1] *= dx[i] + dy[i] + dz[i]
        nv[i >> 1] *= (dx[i] + dy[i] + dz[i]) * -1
        search(nx, ny, nz, nv)
result = set()
dx, dy, dz = [1, -1, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0], [0, 0, 0, 0, 1, -1]
ax = ay = az = -1
m, n, h = map(int, input().split())
graph, visited = [[input() for _ in range(n)] for _ in range(h)], [[[False for _ in range(8)] for _ in range(8)] for _ in range(8)]
for x in range(h):
    for y in range(n):
        for z in range(m):
            if graph[x][y][z] == 'x':
                ax, ay, az = x, y, z
search(ax, ay, az, [1, 2, 3, 4])
print('Yes' if len(result) == 8 else 'No')

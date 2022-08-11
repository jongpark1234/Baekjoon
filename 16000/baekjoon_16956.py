dx, dy = [-1, 1, 0, 0], [0, 0, 1, -1]
r, c = map(int, input().split())
farm = [input().replace('.', 'D') for _ in range(r)]
for y in range(r):
    for x in range(c):
        if farm[y][x] == 'W':
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < c and 0 <= ny < r:
                    if farm[ny][nx] == 'S':
                        print(0)
                        exit(0)
print(1)
for i in farm:
    print(''.join(i))

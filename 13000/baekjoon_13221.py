x, y = map(int, input().split())
print(*min([tuple(map(int, input().split())) for _ in range(int(input()))], key=lambda z: abs(x - z[0]) + abs(y - z[1])))

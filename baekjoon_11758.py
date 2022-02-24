from sys import stdin
point = [list(map(int, stdin.readline().split())) for _ in range(3)]
if (point[1][0] - point[0][0]) * (point[2][1] - point[0][1]) > (point[1][1] - point[0][1]) * (point[2][0] - point[0][0]):
    print(1)
elif (point[1][0] - point[0][0]) * (point[2][1] - point[0][1]) < (point[1][1] - point[0][1]) * (point[2][0] - point[0][0]):
    print(-1)
else:
    print(0)

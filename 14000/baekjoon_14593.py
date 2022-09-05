print(sorted(enumerate([list(map(int, input().split())) for _ in range(int(input()))]), key = lambda x: (-x[1][0], x[1][1], x[1][2]))[0][0] + 1)

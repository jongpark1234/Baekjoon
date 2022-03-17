build = []
result = []
n = int(input())
for _ in range(n):
    build.append(list(map(int, input().split())))
for i in build:
    rank = 1
    for j in build:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    result.append(rank)
print(' '.join(map(str, result)))

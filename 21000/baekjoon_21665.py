result = 0
n, m = map(int, input().split())
Map1 = [input() for _ in range(n)]
input()
Map2 = [input() for _ in range(n)]
for i in range(n):
    for j in range(m):
        if Map1[i][j] == Map2[i][j]:
            result += 1
print(result)

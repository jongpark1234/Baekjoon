n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
m, k = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(m)]
result = [[0 for _ in range(k)] for _ in range(n)]
for N in range(n):
    for K in range(k):
        for M in range(m):
            result[N][K] += a[N][M] * b[M][K]
for i in result:
    print(*i)

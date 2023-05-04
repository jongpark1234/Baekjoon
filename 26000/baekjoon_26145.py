n, m = map(int, input().split())
s = list(map(int, input().split())) + [0 for _ in range(m)]
for i in range(n):
    for idx, j in enumerate(map(int, input().split())):
        s[i] -= j
        s[idx] += j
print(*s)

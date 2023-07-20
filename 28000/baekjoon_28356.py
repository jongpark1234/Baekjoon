n, m = map(int, input().split())
result = [[(4 if j & 1 else 2) if i & 1 else ((2 if n == 1 else 3) if j & 1 else 1) for j in range(m)] for i in range(n)]
print(max(max(result)))
for i in result:
    print(*i)

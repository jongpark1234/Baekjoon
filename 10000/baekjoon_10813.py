n, m = map(int, input().split())
baskets = [i + 1 for i in range(n)]
for _ in range(m):
    i, j = map(lambda x: int(x) - 1, input().split())
    baskets[i], baskets[j] = baskets[j], baskets[i]
print(*baskets)

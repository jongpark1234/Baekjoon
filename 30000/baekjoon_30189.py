n, m = map(int, input().split())
print(sum(sum(x + y == i for y in range(m + 1) for x in range(n + 1)) for i in range(n + m + 1)))

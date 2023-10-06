a, b = map(int, input().split())
k, x = map(int, input().split())
result = sum(abs(i - k) <= x for i in range(a, b + 1))
print(result if result else 'IMPOSSIBLE')

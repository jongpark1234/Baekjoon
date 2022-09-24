n, k, m = map(int, input().split())
a = list(map(int, input().split()))
for _ in range(m):
    i = int(input())
    if i > 0 and i >= k:
        k = i - k + 1
    elif i < 0 and n + i + 1 <= k:
        k = 2 * n - k + i + 1
print(k)

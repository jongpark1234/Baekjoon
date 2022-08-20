while True:
    result = 1
    n, k = map(int, input().split())
    if n == k == 0:
        break
    for i in range(1, min(k, n - k) + 1):
        result = result * n // i
        n -= 1
    print(result)

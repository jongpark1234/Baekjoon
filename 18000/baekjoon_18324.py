k, n = map(int, input().split())
for _ in range(n):
    x = int(input())
    if x * (x + 1) // 2 >= k:
        l, r = 1, x
        while l < r:
            mid = l + r >> 1
            if mid * (mid + 1) // 2 >= k:
                r = mid
            else:
                l = mid + 1
        print(l)
    else:
        X = x * (x - 1) // 2
        l, r = x, 100000
        while l < r:
            mid = l + r >> 1
            if mid * mid - X >= k:
                r = mid
            else:
                l = mid + 1
        print(l * 2 - x - (l * (l - 1) - X >= k))

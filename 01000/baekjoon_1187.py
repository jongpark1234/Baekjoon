def number_game(l, r):
    n = (r - l + 2) // 2
    if n <= 1:
        return a[l]
    h = [number_game(l + i * (n // 2), l + i * (n // 2) + n - 2) // (n // 2) for i in range(3)]
    if h[0] & 1 == h[1] & 1:
        return (h[0] + h[1]) * (n // 2)
    elif h[1] & 1 == h[2] & 1:
        for i in range(n // 2):
            a[l + i], a[l + i + n] = a[l + i + n], a[l + i]
        return (h[1] + h[2]) * (n // 2)
    else:
        for i in range(n // 2):
            a[l + i + n // 2], a[l + i + n] = a[l + i + n], a[l + i + n // 2]
        return (h[0] + h[2]) * (n // 2)
n = int(input())
a = list(map(int, input().split()))
number_game(0, (n - 1) * 2)
print(*a[:n])

# pypy3
for _ in range(int(input())):
    cnt = 0
    n, m = map(int, input().split())
    for b in range(1, n):
        for a in range(1, b):
            if (a ** 2 + b ** 2 + m) / (a * b) == (a ** 2 + b ** 2 + m) // (a * b):
                cnt += 1
    print(cnt)

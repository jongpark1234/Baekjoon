from sys import stdin
for _ in range(int(stdin.readline())):
    k, n, m = map(int, stdin.readline().split())
    ret = False
    if k == 1:
        ret = n & 1 and m & 1
    elif n <= k | m <= k:
        ret = (n & 1 and m & 1) | (n & 1 ^ 1 and m & 1 ^ 1)
    elif n > m:
        if m % (k + 1):
            diff = n - m & 1
            ret = diff if m // (k + 1) & 1 else not diff
    else:
        if n % (k + 1):
            ret = (n & 1 ^ 1 and m & 1) | (n & 1 and m & 1 ^ 1) if n // (k + 1) & 1 else (n & 1 ^ 1 and m & 1 ^ 1) | (n & 1 and m & 1)
    print('cubelover' if ret else 'koosaga')

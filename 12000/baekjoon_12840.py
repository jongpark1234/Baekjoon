from sys import stdin
h, m, s = map(int, stdin.readline().split())
for _ in range(int(stdin.readline())):
    q = list(map(int, stdin.readline().split()))
    if len(q) == 1 and q[0] == 3:
        print(h, m, s)
    else:
        t = (h * 3600 + m * 60 + s) + (q[1] if q[0] == 1 else -q[1])
        if t < 0:
            t += 86400
        t %= 86400
        h, m, s = t // 3600, (t % 3600) // 60, t % 60

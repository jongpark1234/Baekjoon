from sys import stdin
t = 0
s, n, m = map(int, input().split())
for i in range(n + m):
    q = int(stdin.readline())
    if q == 1:
        t += 1
        if t > s:
            s <<= 1
    else:
        t -= 1
print(s)

import sys
c, s = 100, 100
n = int(sys.stdin.readline())
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    if a > b:
        s -= a
    elif b > a:
        c -= b
print(c, s, sep='\n')

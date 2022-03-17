import sys
t = int(sys.stdin.readline())
for i in range(t):
    money = 0
    money += int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    for _ in range(n):
        q, p = map(int, sys.stdin.readline().split())
        money += (q * p)
    print(money)

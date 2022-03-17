import sys
t = int(sys.stdin.readline())
for _ in range(t):
    print(sum(list(map(int, sys.stdin.readline().split(',')))))

import sys
t = int(sys.stdin.readline())
for i in range(t):
    temp = 1
    a, b = map(int, sys.stdin.readline().split())
    b = b % 4 + 4
    for j in range(b):
        temp = (temp * a) % 10
    if temp == 0:
        temp = 10
    print(temp)
    
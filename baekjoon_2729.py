import sys
t = int(sys.stdin.readline())
for i in range(t):
    a, b = map(str, sys.stdin.readline().split())
    a = int(a, 2)
    b = int(b, 2)
    c = a + b
    print(bin(c)[2:])

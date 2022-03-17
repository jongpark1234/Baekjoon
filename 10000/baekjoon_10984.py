import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    t_c = 0
    t_g = 0
    for _ in range(n):
        c, g = map(float, sys.stdin.readline().split())
        t_c += c
        t_g += c * g
    gpa = t_g / t_c
    print(int(t_c), '%.1f' % gpa)

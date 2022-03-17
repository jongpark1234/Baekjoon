import sys
t = int(sys.stdin.readline())
for _ in range(t):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    f0 = [x for x in range(1, n + 1)]
    for i in range(k):
        for j in range(1, n):
            f0[j] += f0[j - 1]
    print(f0[-1])

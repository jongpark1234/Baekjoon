import sys
t = int(sys.stdin.readline())
for i in range(t):
    namelist, consump = [], []
    n = int(sys.stdin.readline())
    for j in range(n):
        a, b = input().rstrip().split()
        namelist.append(a); consump.append(int(b))
    print(namelist[consump.index(max(consump))])

import sys
n, m = map(int, sys.stdin.readline().split())
nlist, mlist = [], []
for _ in range(n):
    nlist.append(sys.stdin.readline().rstrip())
for _ in range(m):
    mlist.append(sys.stdin.readline().rstrip())
plist = list(set(nlist) & set(mlist))
plist.sort()
print(len(plist))
for i in range(len(plist)):
    print(plist[i])

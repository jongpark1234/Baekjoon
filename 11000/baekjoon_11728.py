from sys import stdin
numlist = []
n, m = map(int, stdin.readline().rstrip().split())
for _ in range(2):
    numlist.extend(list(map(int, stdin.readline().rstrip().split())))
numlist.sort()
print(' '.join(list(map(str, numlist))))

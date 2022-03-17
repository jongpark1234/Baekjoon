from sys import stdin
count = 0
n, m = map(int, stdin.readline().split())
s = [stdin.readline().rstrip() for i in range(n)]
strlist = [stdin.readline().rstrip() for i in range(m)]
for i in strlist:
    if i in s:
        count += 1
print(count)

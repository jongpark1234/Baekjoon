import sys
temp, time = 0, 0
n = int(sys.stdin.readline())
p = list(map(int, sys.stdin.readline().split()))
p.sort()
for i in range(len(p)):
    time += temp + p[i]
    temp += p[i]
print(time)

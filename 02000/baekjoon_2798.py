import sys
n, m = map(int, sys.stdin.readline().split())
cardlist = list(map(int, sys.stdin.readline().split()))
temp = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            if cardlist[i] + cardlist[j] + cardlist[k] > m:
                pass
            else:
                temp = max(temp, cardlist[i] + cardlist[j] + cardlist[k])
print(temp)
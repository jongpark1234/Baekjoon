from sys import stdin
result = 0
n = int(input())
xlist, ylist = [], []
for _ in range(n):
    x, y = map(int, stdin.readline().split())
    xlist.append(x)
    ylist.append(y)
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            x1, x2, x3 = xlist[i], xlist[j], xlist[k]
            y1, y2, y3 = ylist[i], ylist[j], ylist[k]
            l1 = pow(x1 - x2, 2) + pow(y1 - y2, 2)
            l2 = pow(x1 - x3, 2) + pow(y1 - y3, 2)
            l3 = pow(x2 - x3, 2) + pow(y2 - y3, 2)
            if l1 == l2 + l3 or l2 == l1 + l3 or l3 == l1 + l2:
                result += 1
print(result)

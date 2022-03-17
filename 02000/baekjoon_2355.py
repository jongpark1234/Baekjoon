a, b = map(int, input().split())
maxnum = max(a, b)
minnum = min(a, b)
dis = maxnum - minnum
print(((dis * (dis + 1)) // 2) + (minnum * (dis + 1)))

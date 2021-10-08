n, x = map(int, input().split())
a = list(map(int, input().split()))
numlist = []
for i in range(len(a)):
    if (a[i] < x):
        numlist.append(a[i])
for j in range(len(numlist)):
    print(numlist[j], end=" ")
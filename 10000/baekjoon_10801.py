alist = list(map(int, input().split()))
blist = list(map(int, input().split()))
a = b = 0
for i in range(10):
    if alist[i] > blist[i]:
        a += 1
    elif blist[i] > alist[i]:
        b += 1
print('DBA'[(a != b) + (a > b)])

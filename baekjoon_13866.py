numlist = list(map(int, input().split()))
t1 = max(numlist) + min(numlist)
numlist.remove(max(numlist))
numlist.remove(min(numlist))
t2 = sum(numlist)
if t1 > t2:
    print(t1 - t2)
else:
    print(t2 - t1)

from collections import deque
from sys import setrecursionlimit
setrecursionlimit(10 ** 6)
def dnc(x, y):
    if x > y:
        return True
    l, r = x, y
    while l <= r:
        if low[l] < x and high[l] > y:
            return dnc(x, l - 1) and dnc(l + 1, y)
        if low[r] < x and high[r] > y:
            return dnc(x, r - 1) and dnc(r + 1, y)
        l += 1
        r -= 1
    return False
for _ in range(int(input())):
    low, high = [0], deque([])
    n = int(input())
    a = [0] + list(map(int, input().split()))
    Dict = {}
    for i in range(1, n + 1):
        low.append(Dict[a[i]] if a[i] in Dict.keys() else 0)
        Dict[a[i]] = i
    Dict.clear()
    for i in range(1, n + 1)[::-1]:
        high.appendleft(Dict[a[i]] if a[i] in Dict.keys() else n + 1)
        Dict[a[i]] = i
    high.appendleft(0)
    print('non-boring' if dnc(1, n) else 'boring')

from random import getrandbits
from collections import defaultdict
idx = 0
numdict, pri = {}, {}
hash = defaultdict(lambda: getrandbits(63) + 1)
n = int(input())
a = map(lambda x: hash[x], input().split())
b = map(lambda x: hash[x], input().split())
a = [i - j for i, j in zip(a, b)]
for i in range(0, n * 2):
    try:
        if pri[idx] + n > i:            
            numdict[idx] += 1
    except KeyError:
        pri[idx] = i
        numdict[idx] = 1
    idx += a[i % n]
print(sum((1 << i) - i - 1 for i in numdict.values()) % 1000000007)

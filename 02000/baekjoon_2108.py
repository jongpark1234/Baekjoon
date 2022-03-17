import sys
from collections import Counter
from math import *
numlist = []
mods = []
n = int(sys.stdin.readline())
for i in range(n):
    numlist.append(int(sys.stdin.readline()))
numlist.sort()
mode = Counter(numlist).most_common()
temp = mode[0][1]
for i in range(len(mode)):
    if mode[i][1] >= temp:
        mods.append(mode[i][0])
    else:
        break
mods.sort()
a = round(sum(numlist) / len(numlist))
b = numlist[len(numlist) // 2]
if len(mods) == 1:
    c = mods[0]
else:
    c = mods[1]
d = max(numlist) - min(numlist)
print(a, b, c, d, sep='\n')

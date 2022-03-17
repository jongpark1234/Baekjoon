from sys import *
from collections import Counter
n = int(stdin.readline())
cardlist = list(map(int, stdin.readline().split()))
m = int(stdin.readline())
findlist = list(map(int, stdin.readline().split()))
count = Counter(cardlist)
for i in findlist:
    print(count[i], end=' ')

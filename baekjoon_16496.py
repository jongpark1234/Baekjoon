from functools import cmp_to_key
from sys import stdin
n = int(stdin.readline())
numlist = sorted(stdin.readline().rstrip().split(), key = cmp_to_key(lambda x, y: 1 if int(x + y) < int(y + x) else -1))
print(''.join(numlist))

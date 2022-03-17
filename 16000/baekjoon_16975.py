# pypy3
from sys import stdin
from math import ceil, log2
def plus(s, e, l, r, node, diff):
    if r < s or l > e:
        return
    if l <= s and e <= r:
        tree[node] += diff
        return
    mid = (s + e) // 2
    plus(s, mid, l, r, node * 2, diff)
    plus(mid + 1, e, l, r, node * 2 + 1, diff)
def find(node):
    global result
    while node:
        result += tree[node]
        node //= 2
n = int(stdin.readline())
size = 2 ** ceil(log2(n))
tree = [0] * (size * 2)
for i, j in enumerate(list(map(int, stdin.readline().split()))):
    tree[size + i] = j
m = int(stdin.readline())
for i in range(m):
    query = list(map(int, stdin.readline().split()))
    if query[0] == 1:
        plus(1, size, query[1], query[2], 1, query[3])
    else:
        result = 0
        find(size + query[1] - 1)
        print(result)

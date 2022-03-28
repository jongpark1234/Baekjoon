# pypy3
from sys import stdin
cnt = 0
tree = {}
keys = []
while True:
    name = stdin.readline().rstrip()
    if not name:
        break
    if name not in keys:
        keys.append(name)
        tree[name] = 1
    else:
        tree[name] += 1
    cnt += 1
for i in sorted(keys):
    print(f'{i} {tree[i] / cnt * 100:.4f}')

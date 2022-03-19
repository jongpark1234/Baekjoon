from sys import stdin
def init(start, end, node):
    if start == end:
        tree[node] = nList[start]
        return tree[node]
    mid = (start + end) // 2
    tree[node] = init(start, mid, node * 2) + init(mid + 1, end, node * 2 + 1)
    return tree[node]
def summit(start, end, node, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return summit(start, mid, node * 2, left, right) + summit(mid + 1, end, node * 2 + 1, left, right)
def update(start, end, node, index, diff):
    if index < start or index > end:
        return
    tree[node] += diff
    if start == end:
        return
    mid = (start+end) // 2
    update(start, mid, node * 2, index, diff)
    update(mid + 1, end, node * 2 + 1, index, diff)
n, m, k = map(int, stdin.readline().split())
nList = []
tree = [0] * ((4 * n))
for i in range(n):
    nList.append(int(stdin.readline()))
init(0, n - 1, 1)
for i in range(m + k):
    cmd = list(map(int, stdin.readline().split()))
    if cmd[0] == 1:
        cmd[1] -= 1
        diff = cmd[2] - nList[cmd[1]]
        nList[cmd[1]] = cmd[2]
        update(0, n - 1, 1, cmd[1], diff)
    elif cmd[0] == 2:
        print(summit(0, n - 1, 1, cmd[1] - 1, cmd[2] - 1))

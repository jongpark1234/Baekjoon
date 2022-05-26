from functools import cmp_to_key
m, n = map(int, input().split())
idx = list(range(n))
result = ['' for _ in range(11)]
sequence = [[] for _ in range(11)]
table = [-1] + [0 for _ in range(100000)]
for i in range(n):
    p = 0
    idx[i] = i
    result[i] = input()
    for j in range(1, len(result[i])):
        while p and result[i][j] != result[i][p]:
            p = table[p]
        if result[i][j] == result[i][p]:
            p += 1
        table[j + 1] = p
    cur = len(result[i])
    while cur >= 0 and cur >= 2 * len(result[i]) - m:
        sequence[i].append(cur)
        cur = table[cur]
idx.sort(key = cmp_to_key(lambda x, y: -1 if [sequence[x], x] < [sequence[y], y] else 1))
for i in range(n):
    print(result[idx[i]])

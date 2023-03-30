MAX = 100
def f(idx: int, v: list[int]) -> int:
    if idx == -1:
        return 0
    if cache[idx] != -1:
        return cache[idx]
    visited = [False for _ in range(MAX + 1)]
    for i in range(k + 1):
        if idx - i < 0:
            break
        toRemove = v[idx - i]
        if idx - i - toRemove >= -1:
            visited[f(idx - i - toRemove, v)] = True
    for i in range(MAX + 1):
        if not visited[i]:
            cache[idx] = i
            return i
    return -1
ret = 0
p, k = map(int, input().split())
for _ in range(p):
    cache = [-1 for _ in range(1001)]
    n, *c = list(map(int, input().split()))
    ret ^= f(n - 1, c)
print('Alice can win.' if ret else 'Bob will win.')

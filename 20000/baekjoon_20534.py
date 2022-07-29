left = [0 for _ in range(1001)]
right = [0 for _ in range(1001)]
numlist = [0 for _ in range(2001)]
fa = [0 for _ in range(2001)]
def find(x: int) -> int:
    if fa[x] == x:
        return x
    find(fa[x])
    numlist[x] ^= numlist[fa[x]]
    fa[x] = fa[fa[x]]
    return fa[x]
def merge(u: int, v: int, f: bool) -> None:
    find(u); find(v)
    if fa[u] == fa[v]:
        if f ^ numlist[u] ^ numlist[v]:
            print('NO')
            exit(0)
        return
    numlist[fa[u]] = f ^ numlist[u]
    fa[fa[u]] = v
n = int(input())
w = list(map(int, input().split()))
for i in range(1, (n << 1) + 1):
    if left[w[i - 1]]:
        right[w[i - 1]] = i
    else:
        left[w[i - 1]] = i
    fa[i], numlist[i] = i, 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i ^ j:
            if left[i] < left[j] and right[j] < right[i]:
                merge(left[j], right[j], False)
            if left[i] < left[j] and left[j] < right[i] and right[i] < right[j]:
                merge(left[j], right[i], True)
for i in range(1, (n << 1) + 1):
    if i == find(i) and numlist[i]:
        print('NO')
        break
else:
    print('YES')
    for i in range(1, n + 1):
        if numlist[left[i]] ^ numlist[right[i]]:
            print(5, 'UD'[numlist[left[i]]], left[i], 'L', left[i] << 1, 'UD'[numlist[left[i]] ^ 1], left[i] + right[i], 'R', left[i] + right[i] , 'UD'[numlist[left[i]]] , right[i])
        else:
            print(3, 'UD'[numlist[left[i]]], right[i] - left[i], 'R', right[i] - left[i], 'UD'[numlist[left[i]] ^ 1], right[i] - left[i])

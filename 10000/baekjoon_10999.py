segment_tree = [0 for _ in range(4040404)]
lazy_propagation = [0 for _ in range(4040404)]
def init(x, s, e):
    if s == e:
        segment_tree[x] = v[s - 1]
        return segment_tree[x]
    m = s + e >> 1
    segment_tree[x] = init(x * 2, s, m) + init(x * 2 + 1, m + 1, e)
    return segment_tree[x]
def updateLazy(x, s, e):
    if lazy_propagation[x]:
        segment_tree[x] += (e - s + 1) * lazy_propagation[x]
        if s != e:
            lazy_propagation[x * 2] += lazy_propagation[x]
            lazy_propagation[x * 2 + 1] += lazy_propagation[x]
        lazy_propagation[x] = 0
def update(x, l, r, s, e, dif):
    updateLazy(x, s, e)
    if e < l or r < s:
        return
    if l <= s and e <= r:
        segment_tree[x] += (e - s + 1) * dif
        if s != e:
            lazy_propagation[x * 2] += dif
            lazy_propagation[x * 2 + 1] += dif
        return
    m = s + e >> 1
    update(x * 2, l, r, s, m, dif)
    update(x * 2 + 1, l, r, m + 1, e, dif)
    segment_tree[x] = segment_tree[x * 2] + segment_tree[x * 2 + 1]
def getSum(x, l, r, s, e):
    updateLazy(x, s, e)
    if e < l or r < s:
        return 0
    if l <= s and e <= r:
        return segment_tree[x]
    m = s + e >> 1
    return getSum(x * 2, l, r, s, m) + getSum(x * 2 + 1, l, r, m + 1, e)
n, q1, q2 = map(int, input().split())
v = []
for i in range(n):
    v.append(int(input()))
init(1, 1, n)
for i in range(q1 + q2):
    q = list(map(int, input().split()))
    if q[0] == 1:
        update(1, q[1], q[2], 1, n, q[3])
    else:
        print(getSum(1, q[1], q[2], 1, n))

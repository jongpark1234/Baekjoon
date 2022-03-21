from math import ceil, log2
from sys import stdin
def segment(idx, l, r):
    if l == r:
        seg[idx] = H[l]
        return seg[idx]
    mid = (l + r) // 2
    l = segment(idx * 2, l, mid)
    r = segment(idx * 2 + 1, mid + 1, r)
    seg[idx] = min(l, r)
    return seg[idx]
def search(From, To):
    if From == To:
        return H[From]
    mid = (From + To) // 2
    l = search(From, mid)
    r = search(mid + 1, To)
    value = max(l, r)
    h = min(H[mid], H[mid + 1])
    w = 2
    s = w * h
    i, j = mid, mid + 1
    while From < i or j < To:
        if j == To or From < i and H[i - 1] >= H[j + 1]:
            i -= 1
            w += 1
            h = min(h, H[i])
            s = max(s, w * h)
        else:
            j += 1
            w += 1
            h = min(h, H[j])
            s = max(s, w * h)
    value = max(value, s)
    return value
n = int(stdin.readline())
H = [int(stdin.readline()) for _ in range(n)]
seg = [0 for _ in range(1 << (ceil(log2(n)) + 1))]
segment(1, 0, len(H) - 1)
print(search(0, len(H) - 1))

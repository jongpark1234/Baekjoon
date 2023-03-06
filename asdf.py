class MultiSegmentTree:
    def __init__(self, h):
        self.h = h
        self.seg = [[0 for _ in range(h << 1)] for _ in range(h << 1)]
    def update(self, x1, y1, d):
        i, j = y1 + self.h - 1, x1 + self.h - 1
        self.seg[i][j] = d
        while j > 1:
            j >>= 1
            self.seg[i][j] = self.seg[i][j << 1] + self.seg[i][(j << 1) + 1]
        while i > 1:
            j = x1 + self.h - 1
            i >>= 1
            self.seg[i][j] = self.seg[i << 1][j] + self.seg[(i << 1) + 1][j]
            while j > 1:
                j >>= 1
                self.seg[i][j] = self.seg[i][j << 1] + self.seg[i][(j << 1) + 1]
    def query_x(self, y, nodeL, nodeR, nodeNum, l, r):
        if nodeL <= l and r <= nodeR:
            return self.seg[y][nodeNum]
        elif nodeR < l or r < nodeL:
            return 0
        mid = l + r >> 1
        return self.query_x(y, nodeL, nodeR, nodeNum << 1, l, mid) + self.query_x(y, nodeL, nodeR, (nodeNum << 1) + 1, mid + 1, r)
    def query_y(self, nodeL, nodeR, nodeNum, l, r, x1, x2):
        if nodeL <= l and r <= nodeR:
            return self.query_x(nodeNum, x1, x2, 1, 1, self.h)
        elif nodeR < l or r < nodeL:
            return 0
        mid = l + r >> 1
        return self.query_y(nodeL, nodeR, nodeNum << 1, l, mid, x1, x2) + self.query_y(nodeL, nodeR, (nodeNum << 1) + 1, mid + 1, r, x1, x2)
h = 1
arr = [[0 for _ in range(1025)] for _ in range(1025)]
n, m = map(int, input().split())
while h < n:
    h <<= 1
segTree = MultiSegmentTree(h)
for i in range(1, n + 1):
    Input = list(map(int, input().split()))
    for j in range(1, n + 1):
        arr[i][j] = Input[j - 1]
        segTree.update(i, j, arr[i][j])
for i in range(m):
    w, *Input = map(int, input().split())
    if w == 0:
        segTree.update(*Input)
    else:
        x1, y1, x2, y2 = Input
        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1
        print(segTree.query_y(y1, y2, 1, 1, h, x1, x2))

class UF:
    def __init__(self, size):
        self.parent = [-1 for _ in range(size)]
    def union(self, x, y, raising = False):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            if raising:
                raise ValueError()
            else:
                return root_x
        if self.parent[root_x] > self.parent[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_x] += self.parent[root_y]
        self.parent[root_y] = root_x
        return root_x
    def find(self, x):
        while (p := self.parent[x]) >= 0:
            x, self.parent[x] = p, self.parent[p]
        return x
def MST(cnt, edge1, edge2):
    ret = 0
    dsu = UF(cnt)
    for edge, cost in [[edge1, 0], [edge2, 1]]:
        for u, v in edge:
            try:
                dsu.union(u, v, raising = True)
            except:
                continue
            ret += cost
            cnt -= 1
            if cnt == 1:
                return ret
while True:
    n, m, k = map(int, input().split())
    if n == 0:
        break
    red, blue = [], []
    for _ in range(m):
        c, f, t = input().split()
        f, t = int(f) - 1, int(t) - 1
        if c == 'R':
            red.append([f, t])
        else:
            blue.append([f, t])
    print('01'[MST(n, red, blue) <= k <= n - 1 - MST(n, blue, red)])

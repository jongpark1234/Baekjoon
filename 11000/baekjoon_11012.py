from sys import stdin
class fanwick:
    def __init__(self, Max):
        if isinstance(Max, int):
            self.length = 1 << ((Max + 1).bit_length())
            self.numlist = [0 for _ in range(self.length)]
            self.tree = [0 for _ in range(self.length)]
        else:
            self.numlist = list(Max)
            self.length = 1 << ((len(self.numlist) + 1).bit_length())
            self.numlist += [0] * (self.length - len(self.numlist)) 
            self.tree = self.numlist[:]
            for i, j in enumerate(self.tree):
                if i | (i + 1) < self.length:
                    self.tree[i | (i + 1)] += j
    def add(self, num, count = 1):
        self.numlist[num] += count
        while num < self.length:
            self.tree[num] += count
            num |= num + 1
    def cnt(self, num):
        ret = 0
        r = num - 1
        while r >= 0:
            ret += self.tree[r]
            r = (r & (r + 1)) - 1
        return ret
for _ in range(int(input())):
    result = 0
    numlist = []
    n, m = map(int, stdin.readline().split())
    for _ in range(n):
        x, y = map(int, stdin.readline().split())
        numlist.append([x, 1, y])
    for _ in range(m):
        l, r, b, t = map(int, stdin.readline().split())
        numlist.append([l, 0, b, t])
        numlist.append([r, 2, b, t])
    tree = fanwick(max([i[-1] for i in numlist]))
    for i in sorted(numlist):
        if i[1] == 1:
            tree.add(i[2])
        else:
            b, t = i[2:]
            cnt = (tree.cnt(t + 1) - tree.cnt(b))
            if i[1] == 0:
                result -= cnt
            else:
                result += cnt
    print(result)

from sys import setrecursionlimit, stdin
class Tree:
    def __init__(self, key):
        self.left = self.right = self.parent = None
        self.key = key
    def getf(self):
        cur = self.right
        while cur.left:
            cur = cur.left
        return cur
    def next(self):
        if self.right:
            return self.getf()
        cur = self
        while cur.parent and cur.parent.right == cur:
            cur = cur.parent
        return cur.parent
    def popped(self, tree):
        if self.right and self.left:
            follower = self.getf()
            follower.popped(tree)
            follower.left = self.left
            follower.right = self.right
            follower.left.parent = follower
            if follower.right:
                follower.right.parent = follower
        elif self.right:
            follower = self.right
        elif self.left:
            follower = self.left
        else:
            follower = None
        if follower:
            follower.parent = self.parent
        if self == tree.root:
            tree.root = follower
        else:
            if self.parent.key < self.key:
                self.parent.right = follower
            else:
                self.parent.left = follower
    def turnLeft(self):
        son = self.right
        parent = self.parent
        self.right = son.left
        if son.left:
            son.left.parent = self
        son.left = self
        self.parent = son
        son.parent = parent
        if parent:
            if parent.key < self.key:
                parent.right = son
            else:
                parent.left = son
    def turnRight(self):
        son = self.left
        parent = self.parent
        self.left = son.right
        if son.right:
            son.right.parent = self
        son.right = self
        self.parent = son
        son.parent = parent
        if parent:
            if parent.key < self.key:
                parent.right = son
            else:
                parent.left = son
    def insertf(self):
        if not self.parent:
            self.wred = False
            return
        if not self.parent.wred:
            return
        parent, grandParent = self.parent, self.parent.parent
        uncle = grandParent.right if self.parent == grandParent.left else grandParent.left
        if uncle and uncle.wred:
            self.parent.wred = False
            uncle.wred = False
            grandParent.wred = True
            grandParent.insertf()
        elif self == parent.right and parent == grandParent.left:
            parent.turnLeft()
            parent.insertf()
        elif self == parent.left and parent == grandParent.right:
            parent.turnRight()
            parent.insertf()
        else:
            if self == parent.left:
                grandParent.turnRight()
            else:
                grandParent.turnLeft()
            grandParent.wred = True
            parent.wred = False
    def popf(parent, x):
        if x == parent.left:
            brother = parent.right
            if brother.wred:
                parent.turnLeft()
                parent.wred, brother.wred = brother.wred, parent.wred
                parent.popf(x)
                return
            elif brother.right and brother.right.wred:
                parent.turnLeft()
                parent.wred, brother.wred = brother.wred, parent.wred
                brother.right.wred = False
                return
            elif brother.left and brother.left.wred:
                brother.turnRight()
                brother.wred = True
                brother.parent.wred = False
                parent.popf(x)
                return
        else:
            brother = parent.left
            if brother.wred:
                parent.turnRight()
                parent.wred, brother.wred = brother.wred, parent.wred
                parent.popf(x)
                return
            elif brother.left and brother.left.wred:
                parent.turnRight()
                parent.wred, brother.wred = brother.wred, parent.wred
                brother.left.wred = False
                return
            elif brother.right and brother.right.wred:
                brother.turnLeft()
                brother.wred = True
                brother.parent.wred = False
                parent.popf(x)
                return
        brother.wred = True
        if parent.wred:
            parent.wred = False
        else:
            if not parent.parent:
                return
            parent.parent.popf(parent)
class BinarySearchTree:
    def __init__(self):
        self.root = None
    def find(self, key):
        cur = self.root
        while cur:
            if cur.key < key:
                cur = cur.right
            elif key < cur.key:
                cur = cur.left
            else:
                break
        return cur
    def insert(self, node):
        cur = self.root
        while cur:
            if cur.key < node.key:
                if cur.right:
                    cur = cur.right
                else:
                    cur.right = node
                    node.parent = cur
                    return
            elif node.key < cur.key:
                if cur.left:
                    cur = cur.left
                else:
                    cur.left = node
                    node.parent = cur
                    return
            else:
                return
        self.root = node
        return
    def pop(self, key):
        cur = self.find(key)
        if not cur:
            return None
        cur.popped(self)
        return cur
    def find_smallest(self):
        cur = self.root
        if not cur:
            return None
        while cur.left:
            cur = cur.left
        return cur
class RedBlackTree(BinarySearchTree):
    def insert(self, node):
        super().insert(node)
        node.wred = True
        node.insertf()
        cur = self.root
        while cur.parent:
            cur = cur.parent
        self.root = cur
    def pop(self, key):
        cur = self.find(key)
        if not cur:
            return
        if cur.left and cur.right:
            follower = cur.getf()
            p_node = follower.right
            if follower == cur.right:
                p_parent = follower
            else:
                p_parent = follower.parent
        else:
            if cur.left:
                follower = cur.left
            else:
                follower = cur.right
            p_node = follower
            p_parent = cur.parent
        if follower and follower.wred:
            follower.wred = cur.wred
            cur.popped(self)
            return cur
        if not cur.left or not cur.right:
            cur.popped(self)
            if cur.wred:
                return cur
            else:
                if not p_parent:
                    return cur
        else:
            follower.wred = cur.wred
            cur.popped(self)
            if p_node and p_node.wred:
                p_node.wred = False
                return cur
            else:
                pass
        p_parent.popf(p_node)
        ascender = self.root
        while ascender.parent:
            ascender = ascender.parent
        self.root = ascender
        return cur
def union(temp, idx):
    parentlist[idx] = temp
    shardlist[idx] -= shardlist[temp]
def find(idx):
    if mlist[idx] != idx:
        mlist[idx] = find(mlist[idx])
    return mlist[idx]
def zip1(idx):
    if idx == parentlist[idx]:
        return 0
    shardlist[idx] += zip1(parentlist[idx])
    parentlist[idx] = parentlist[parentlist[idx]]
    return shardlist[idx]
def zip2(idx, cnt):
    if idx == parentlist[idx]:
        return 0
    if cnt == 100:
        return shardlist[idx]
    shardlist[idx] += zip2(parentlist[idx], cnt + 1)
    parentlist[idx] = parentlist[parentlist[idx]]
    return shardlist[idx]
def path_sum(idx):
    return zip1(idx) + shardlist[parentlist[idx]]
def Get(idx):
    ret, cur = 0, deadlinetree.root
    while cur:
        ret += cur.segment
        if deadlinelist[idx] < cur.key:
            cur = cur.left
        elif cur.key < deadlinelist[idx]:
            cur = cur.right
        else:
            break
    while parentlist[idx] != parentlist[parentlist[idx]]:
        zip2(idx, 0)
    return deadlinelist[idx] - ret * t - path_sum(idx)
setrecursionlimit(10 ** 6)
n, t = map(int, stdin.readline().split())
photolist = sorted([[*map(int, stdin.readline().split())] for _ in range(n)])
deadline = float('inf')
deadlinelist = []
for _, time, idx in sorted([[time[0], time[1], idx] for idx, time in enumerate(photolist)], key = lambda x: x[1]):
    if time != deadline:
        deadline = time
        deadlinelist.append(deadline)
    photolist[idx].append(len(deadlinelist) - 1)
deadlinetree = RedBlackTree()
for i in deadlinelist:
    node = Tree(i)
    node.segment = 0
    deadlinetree.insert(node)
shardlist = [0 for _ in range(len(deadlinelist))]
eqlist = [i - 1 for i in range(len(deadlinelist))]
parentlist = [i for i in range(len(deadlinelist))]
mlist = [i for i in range(len(deadlinelist))]
RBTree = RedBlackTree()
able = len(deadlinelist)
key = photolist[-1][-1]
for i in range(n - 1, -1, -1):
    while able:
        if deadlinelist[able - 1] <= photolist[i][0]:
            break
        able -= 1
        pc = deadlinelist[able] % t
        node = RBTree.find(pc)
        if node:
            union(node.r, able)
        else:
            node = Tree(pc)
            node.r = able
            RBTree.insert(node)
    deadline, cur = photolist[i][1], deadlinetree.root
    while True:
        if cur.key < deadline:
            cur = cur.right
            continue
        cur.segment += 1
        if cur.left:
            cur.left.segment -= 1
            if cur.key != deadline:
                cur = cur.left
                continue
        break
    pos = find(photolist[i][2])
    key, uc = min(pos, key), Get(pos)
    while eqlist[pos] >= 0:
        if Get(eqlist[pos]) < uc:
            break
        mlist[eqlist[pos]], eqlist[pos] = pos, eqlist[eqlist[pos]]
    if mlist[key] != key:
        key = pos
    lc = Get(key)
    if lc < photolist[i][0]:
        print('no')
        break
    if photolist[i][0] + t <= lc:
        continue
    left, right = lc % t, photolist[i][0] % t
    enlf = RBTree.find(left)
    if left < right:
        if not enlf:
            enlf = Tree(left)
            RBTree.insert(enlf)
            candidate = enlf.next()
            if candidate and candidate.key < right:
                enlf.r = candidate.r
                shardlist[candidate.r] += candidate.key - left
                RBTree.pop(candidate.key)
            else:
                RBTree.pop(enlf.key)
                continue
        while True:
            candidate = enlf.next()
            if not candidate:
                break
            if right <= candidate.key:
                break
            union(enlf.r, candidate.r)
            shardlist[candidate.r] += candidate.key - left
            RBTree.pop(candidate.key)
    else:
        if not enlf:
            enlf = Tree(left)
            RBTree.insert(enlf)
            candidate = enlf.next()
            if not candidate:
                smallest = RBTree.find_smallest()
                if smallest.key < right:
                    candidate = smallest
            if candidate:
                enlf.r = candidate.r
                shardlist[candidate.r] += (candidate.key - left) % t
                RBTree.pop(candidate.key)
            else:
                RBTree.pop(enlf.key)
                continue
        while True:
            candidate = enlf.next()
            if not candidate:
                break
            union(enlf.r, candidate.r)
            shardlist[candidate.r] += candidate.key - left
            RBTree.pop(candidate.key)
        while True:
            candidate = RBTree.find_smallest()
            if not candidate.key < right:
                break
            union(enlf.r, candidate.r)
            shardlist[candidate.r] += (candidate.key - left) % t
            RBTree.pop(candidate.key)
else:
    print('yes')

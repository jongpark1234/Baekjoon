# pypy3
from sys import stdin
class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = {}
        self.right = {}
class Trie(object):
    def __init__(self):
        self.head = Node(0)
    def insert(self, cmd):
        s = self.head
        for i in cmd:
            if i == '0':
                if s.left:
                    s.left.data += 1
                else:
                    s.left = Node(0)
                s = s.left
            else:
                if s.right:
                    s.right.data += 1
                else:
                    s.right = Node(0)
                s = s.right  
    def delete(self, cmd):
        s = self.head
        for i in cmd:
            if i == '0':
                if s.left.data > 0:
                    s.left.data -= 1
                else:
                    s.left = False
                    break
                s = s.left
            else:
                if s.right.data > 0:
                    s.right.data -= 1
                else:
                    s.right = False
                    break
                s = s.right
    def xor(self, cmd):
        s = self.head
        ans = '0b'
        for i in cmd:
            if i == '0':
                if s.right :
                    ans += '1'
                    s = s.right
                else:
                    ans += '0'
                    s = s.left
            else:
                if s.left :
                    ans += '1'
                    s = s.left 
                else:
                    ans += '0'
                    s = s.right
        answer = int(ans,2)
        return answer
n = int(stdin.readline())
trie = Trie()
t = format(0,'b').zfill(30)
trie.insert(t)
for _ in range(n):
    query, x = map(int, stdin.readline().split())
    cmd = format(x,'b').zfill(30)
    if query == 1:
        trie.insert(cmd)
    elif query == 2:
        trie.delete(cmd)
    elif query == 3:
        result = trie.xor(cmd)
        print(result)

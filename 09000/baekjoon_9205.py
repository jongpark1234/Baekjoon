from collections import deque
class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
for _ in range(int(input())):
    n = int(input())
    home = Position(*map(int, input().split()))
    conveniences = [Position(*map(int, input().split())) for _ in range(n)]
    visited = [False for _ in range(n)]
    festival = Position(*map(int, input().split()))
    queue = deque([home])
    while queue:
        now: Position = queue.popleft()
        if abs(now.x - festival.x) + abs(now.y - festival.y) <= 1000:
            print('happy')
            break
        for i in range(n):
            if visited[i]:
                continue
            convenience = conveniences[i]
            if abs(now.x - convenience.x) + abs(now.y - convenience.y) <= 1000:
                queue.append(convenience)
                visited[i] = True
    else:
        print('sad')

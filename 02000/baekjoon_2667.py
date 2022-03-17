from sys import setrecursionlimit
setrecursionlimit(10 ** 6)
n = int(input())
graph = []
areas = []
for i in range(n):
    graph.append(list(map(int, input())))
def search(x, y):
    global area
    if x <= -1 or x >= n or y <= -1 or y >= n: 
        return False
    if graph[x][y] == 1:
        graph[x][y] = 0
        area += 1
        search(x - 1, y)
        search(x, y - 1)
        search(x + 1, y)
        search(x, y + 1)
        return True
    else:
        return False
count = 0 
for i in range(n):
    for j in range(n):
        area = 0
        if search(i, j) == True:
            count += 1
            areas.append(area)
print(count) 
print('\n'.join(map(str, sorted(areas))))

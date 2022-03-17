import sys
board1 = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]
board2 = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
          ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
          ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]
n, m = map(int, sys.stdin.readline().split())
field = [[] for _ in range(n)]
for i in range(n):
    line = sys.stdin.readline().strip()
    for j in range(m):
        field[i].append(line[j])
result = 64
for i in range(n - 7):
    for j in range(m - 7):
        count1 = 0
        count2 = 0
        for r in range(8):
            for c in range(8):
                if field[i + r][j + c] != board1[r][c]:
                    count1 += 1
                if field[i + r][j + c] != board2[r][c]: 
                    count2 += 1
        result = min(result, count1, count2)
print(result)

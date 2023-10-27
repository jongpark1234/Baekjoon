result = cur = 0
n, m, l = map(int, input().split())
visited = [0 for _ in range(n)]
while True:
    visited[cur] += 1
    if visited[cur] == m:
        break
    cur = (cur + l * (-1 if visited[cur] & 1 else 1)) % n 
    result += 1
print(result)

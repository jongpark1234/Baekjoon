result = turn = 0
n, k = map(int, input().split())
visited = [False for _ in range(n)]
pointed = [int(input()) for _ in range(n)]
while True:
    if pointed[turn] == k:
        print(result + 1)
        break
    if visited[pointed[turn]]:
        print(-1)
        break
    turn = pointed[turn]
    visited[turn] ^= 1
    result += 1

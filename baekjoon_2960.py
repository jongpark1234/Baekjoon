n, k = map(int, input().split())
count = 0
found = False
visited = {}
for i in range(2, n + 1):
    for j in range(i, n + 1, i):
        try:
            visited[j] += 1
        except KeyError:
            visited[j] = 1
            count += 1
            if count == k:
                found = True
                print(j)
                break
    if found:
        break

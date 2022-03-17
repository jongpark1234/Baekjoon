# pypy3
N, M = map(int, input().split())
numlist = sorted(list(map(int, input().split())))
visited = [False] * N
out = []
all_out = []
def solve(depth, N, M):
    if depth == M:
        tmp = ' '.join(map(str, out))
        if tmp not in all_out:
            all_out.append(tmp)
        return
    for i in range(N):
        if not visited[i]:
            out.append(numlist[i])
            visited[i] = True
            solve(depth+1, N, M)
            out.pop()
            visited[i] = False
solve(0, N, M)
for i in all_out:
    print(i)

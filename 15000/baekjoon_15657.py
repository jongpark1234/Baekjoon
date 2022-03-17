n, m = map(int, input().split())
numlist = list(map(int, input().split()))
numlist.sort()
solve = []
def Dfs(depth):
    if depth == m:
        print(' '.join(map(str, solve)))
        return
    for i in range(n):
        if depth == 0 or solve[depth - 1] <= numlist[i]:
            solve.append(numlist[i])
            Dfs(depth + 1)
            solve.pop()
Dfs(0)
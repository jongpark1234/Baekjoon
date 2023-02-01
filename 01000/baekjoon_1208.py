def dfs1(Sum, current, end):
    if current == end:
        countDict[Sum] = countDict.get(Sum, 0) + 1
        return
    dfs1(Sum, current + 1, end)
    dfs1(Sum + numlist[current], current + 1, end)
def dfs2(Sum, current, end):
    global result
    if current == end:
        result += countDict[S - Sum] if S - Sum in countDict else 1 if Sum == S else 0
        return
    dfs2(Sum, current + 1, end)
    dfs2(Sum + numlist[current], current + 1, end)
result = 0
N, S = map(int, input().split())
numlist = list(map(int, input().split()))
countDict = dict()
m = N >> 1
dfs1(0, 0, m)
dfs2(0, m, N)
print(result - (S == 0))

n, m = map(int, input().split())
numlist = list(map(int, input().split()))
dup_check = []
def solve(num, start, ans):
    if len(ans) == num:
        for i in ans:
            print(numlist[i], end=' ')
        print()
        return
    for i in range(start,len(numlist)):
        solve(num, i, ans + [i])
numlist = sorted(list(set(numlist)))
for i in range(len(numlist)):
    solve(m, i, [i])

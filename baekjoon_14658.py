import sys
input = sys.stdin.readline
n, m, l, k = map(int, input().split())
star = [list(map(int, input().split())) for _ in range(k)]
Max = 0
for i in range(k):
    for j in range(k):
        cnt = 0
        for K in range(k):
            if star[i][0] <= star[K][0] and star[K][0] <= star[i][0] + l and star[j][1] <= star[K][1] and star[K][1] <= star[j][1] + l:
                cnt += 1
                Max = max(cnt, Max)
print(k - Max)

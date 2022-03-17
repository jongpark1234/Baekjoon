# pypy3
def add(x):
    global cnt2
    count[cnt1[numlist[x]]] -= 1
    cnt1[numlist[x]] += 1
    count[cnt1[numlist[x]]] += 1
    cnt2 = max(cnt2, cnt1[numlist[x]])
def sub(x):
    global cnt2
    count[cnt1[numlist[x]]] -= 1
    if cnt2 == cnt1[numlist[x]] and count[cnt1[numlist[x]]] == 0:
        cnt2 -= 1
    cnt1[numlist[x]] -= 1
    count[cnt1[numlist[x]]] += 1
n = int(input())
VALUE = 100000
cnt2 = 0
numlist = [0] + list(map(int, input().split()))
m = int(input())
query = sorted([list(map(int, input().split())) + [i] for i in range(m)], key = lambda x: [x[0] // n ** 0.5, x[1]])
cnt1 = [0 for _ in range(VALUE + 1)]
count = [0 for _ in range(VALUE + 1)]
visit = [0 for _ in range(VALUE + 1)]
result = [0 for _ in range(m)]
for i in range(n):
    if visit[i] == 0:
        count[0] += 1
    visit[i] += 1
s, e = query[0][0], query[0][1]
for i in range(s, e + 1):
    add(i)
result[query[0][2]] = cnt2
for i in range(1, m):
    qs, qe, idx = query[i]
    while qs < s:
        s -= 1
        add(s)
    while qs > s:
        sub(s)
        s += 1
    while e < qe:
        e += 1
        add(e)
    while e > qe:
        sub(e)
        e -= 1
    result[idx] = cnt2
for i in range(m):
    print(result[i])

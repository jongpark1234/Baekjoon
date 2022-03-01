# pypy3
cnt = 0
n = int(input())
capitals = list(map(int, input().split()))
Sum = sum(capitals)
for i in range(n):
    capital = capitals[i]
    if capital < 0:
        cnt += -(capital + 1) // Sum + 1
    j = (i + 1) % n
    while i != j:
        capital += capitals[j]
        if capital < 0:
            cnt += -(capital + 1) // Sum + 1
        j = (j + 1) % n
print(cnt)

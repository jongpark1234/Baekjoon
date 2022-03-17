from sys import stdin
cnt = 0
party = []
n, m = map(int, stdin.readline().split())
witness = set(stdin.readline().rstrip().split()[1:])
for _ in range(m):
    party.append(set(stdin.readline().rstrip().split()[1:]))
for _ in range(m):
    for i in party:
        if i & witness:
            witness = witness.union(i)
for i in party:
    if i & witness:
        continue
    cnt += 1
print(cnt)

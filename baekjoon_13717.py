name = []
evolution = []
for _ in range(int(input())):
    name.append(input())
    k, m = map(int, input().split())
    times = 0
    while m >= k:
        m -= k
        m += 2
        times += 1
    evolution.append(times)
print(sum(evolution))
print(name[evolution.index(max(evolution))])

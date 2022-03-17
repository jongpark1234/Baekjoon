n = int(input())
a1 = list(map(int, input().split()))
a2 = sorted(a1)
a = []
for i in range(n):
    idx = a2.index(a1[i])
    a.append(idx)
    a2[idx] = -1
print(*a)

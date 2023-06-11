n = int(input())
a = list(map(int, input().split()))
idx = a.index(max(a))
ascend, descend = a[:idx], a[idx:]
print('YES' if ascend == sorted(ascend) and descend == sorted(descend, reverse=True) and len(set(ascend)) == len(ascend) and len(set(descend)) == len(descend) else 'NO')

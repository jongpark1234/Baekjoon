n = int(input())
k = [int(input()) - 1 for _ in range(n)]
print(*[k.index(i) + 1 for i in range(n)])

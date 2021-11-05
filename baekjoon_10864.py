n, m = map(int, input().split())
friend = [0 for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    friend[a - 1] += 1
    friend[b - 1] += 1
print('\n'.join(list(map(str, friend))))

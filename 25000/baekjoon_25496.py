p, n = map(int, input().split())
a = sorted(map(int, input().split()))
for i in range(n):
    if p + sum(a[:i]) > 199:
        print(i)
        break
else:
    print(n)

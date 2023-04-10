n, m = map(int, input().split())
for _ in range(m):
    k = int(input())
    dummy = list(map(int, input().split()))
    if dummy != sorted(dummy, reverse=True):
        print('No')
        break
else:
    print('Yes')

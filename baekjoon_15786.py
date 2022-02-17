n, m = map(int, input().split())
s = input()
for _ in range(m):
    idx = 0
    p = input()
    for i in p:
        if i == s[idx]:
            idx += 1
        if idx == n:
            break
    print('true' if idx == n else 'false')

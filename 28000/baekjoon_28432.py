n = int(input())
s = [input() for _ in range(n)]
idx = s.index('?')
start, end = s[idx - 1][-1] if idx > 0 else '!', s[idx + 1][0] if idx < n - 1 else '!'
for i in [input() for _ in range(int(input()))]:
    if i in s:
        continue
    if (i[0] == start or start == '!') and (i[-1] == end or end == '!'):
        print(i)
        break

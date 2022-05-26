def sfx(s):
    ret, j = [0 for _ in range(len(s))], 0
    for i in range(1, len(s)):
        while j > 0 and s[i] != s[j]:
            j = ret[j - 1]
        if s[i] == s[j]:
            ret[i] = j + 1
            j += 1
        else:
            ret[i] = 0
    return ret
result = []
s = input()
ret = sfx(s)
cnt = [0 for _ in range(len(s) + 1)]
for i in range(len(s)):
    cnt[ret[i]] += 1
for i in range(1, len(s) + 1)[::-1]:
    cnt[ret[i - 1]] += cnt[i]
Len = len(s)
while Len > 0:
    result.append([Len, cnt[Len] + 1])
    Len = ret[Len - 1]
print(len(result))
for i in result[::-1]:
    print(*i)

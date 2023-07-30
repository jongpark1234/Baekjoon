t, s = [], []
for _ in range(int(input())):
    ti, si = map(int, input().split())
    t.append(ti)
    s.append(si)
f = s.index(max(s))
print(0 if s[f] == 0 else t[f] + f * 20)

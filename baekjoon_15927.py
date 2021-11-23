s = input()
same = True
for i in range(len(s) - 1):
    if s[i] != s[i + 1]:
        same = False
        break
if same:
    print(-1)
elif s == s[::-1]:
    print(len(s) - 1)
elif s != s[::-1]:
    print(len(s))

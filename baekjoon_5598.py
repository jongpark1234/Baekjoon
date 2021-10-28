s = list(map(str, input()))
for i in range(len(s)):
    if ord(s[i]) > 67:
        s[i] = chr(ord(s[i]) - 3)
    else:
        s[i] = chr(ord(s[i]) + 23)
for i in range(len(s)):
    print(s[i], end='')

s = list(map(str, input()))
for i in range(len(s)):
    if s[i].islower():
        s[i] = chr(ord(s[i]) - 32)
    else:
        s[i] = chr(ord(s[i]) + 32)
    print(s[i], end='')

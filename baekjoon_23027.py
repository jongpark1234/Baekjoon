s = list(input())
if 'A' in s:
    for i in range(len(s)):
        if s[i] == 'B' or s[i] == 'C' or s[i] == 'D' or s[i] == 'F':
            s[i] = 'A'
elif 'B' in s:
    for i in range(len(s)):
        if s[i] == 'C' or s[i] == 'D' or s[i] == 'F':
            s[i] = 'B'
elif 'C' in s:
    for i in range(len(s)):
        if s[i] == 'D' or s[i] == 'F':
            s[i] = 'C'
else:
    for i in range(len(s)):
        s[i] = 'A'
print(''.join(s))

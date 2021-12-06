s = list(input())
idx = 0
start = 0
while idx < len(s):
    if s[idx] == '<':
        idx += 1
        while s[idx] != '>':
            idx += 1
        idx += 1
    elif s[idx].isalnum():
        start = idx
        while idx < len(s) and s[idx].isalnum():
            idx += 1
        s[start:idx] = s[start:idx][::-1]
    else:
        idx += 1
print(''.join(s))

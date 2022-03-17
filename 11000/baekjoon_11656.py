from sys import stdin
suffix = []
s = stdin.readline().rstrip()
for i in range(len(s)):
    suffix.append(s[i:])
print('\n'.join(sorted(suffix)))

from sys import stdin
string = '#' + '#'.join(stdin.readline().rstrip()) + '#'
n = len(string)
a = [0] * n
c = 0; r = 0
for i in range(n):
    a[i] = 0 if r < i else min(a[(2 * c) - i], r - i)
    while i - 1 - a[i] >= 0 and i + 1 + a[i] < n and string[i - 1 - a[i]] == string[i + 1 + a[i]]:
        a[i] = a[i] + 1
    if (r < i + a[i]):
        r = i + a[i]
        c = i
print(max(a))

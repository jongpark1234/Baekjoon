def getTable(pattern, length):
    table, j = [0 for _ in range(length)], 0
    for i in range(1, len(pattern)):
        while j and pattern[i] != pattern[j]:
            j = table[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
    return table[:]
def kmp(s, p):
    ret = j = 0
    n, m = len(s), len(p)
    fail = getTable(p, m)
    for i in range(n):
        while j and s[i] != p[j]:
            j = fail[j - 1]
        if s[i] == p[j]:
            if j == m - 1:
                ret += 1
                j = fail[j]
            else:
                j += 1
    return ret
tc = 0
fibonacci = ['0', '1']
for i in range(2, 31):
    fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
while True:
    try:
        tc += 1
        n, p = int(input()), input()
        dp = [+(p == '0'), +(p == '1')] + [kmp(fibonacci[i], p) for i in range(2, 28)]
        s1, s2 = fibonacci[27][len(fibonacci[27]) - len(p) + 1:] + fibonacci[26][:len(p) - 1], fibonacci[26][len(fibonacci[26]) - len(p) + 1:] + fibonacci[27][:len(p) - 1]
        match = [kmp(s1, p), kmp(s2, p)]
        flag = 0
        for i in range(28, n + 1):
            dp.append(dp[i - 1] + dp[i - 2] + match[flag])
            flag ^= 1
        print(f'Case {tc}: {dp[n]}')
    except EOFError:
        break

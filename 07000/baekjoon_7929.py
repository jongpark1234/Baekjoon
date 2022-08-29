def solve(s):
    i = idx = 0
    n = len(s)
    while i < n >> 1:
        idx, j, k = i, i + 1, i
        while j < n and s[k] <= s[j]:
            j, k = j + 1, i if s[k] < s[j] else k + 1
        while i <= k:
            i += j - k
    return s[idx:idx + (n >> 1)]
for _ in range(int(input())):
    print(solve(input() * 2))

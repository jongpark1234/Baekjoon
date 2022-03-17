def getTable(pattern):
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
def kmp(s, pattern):
    getTable(pattern)
    j = 0
    for i in range(len(s)):
        while j > 0 and s[i] != pattern[j]:
            j = table[j - 1]
        if s[i] == pattern[j]:
            if j == len(pattern) - 1:
                return 1
            else:
                j += 1
    return 0
s = input()
pattern = input()
table = [0 for _ in range(len(pattern))]
print(kmp(s, pattern))

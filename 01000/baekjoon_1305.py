def KMP(pattern):
    table = [0 for _ in range(len(pattern))]
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            table[i] = j
    return table
n = int(input())
print(n - KMP(input())[n - 1])
MAX = 3001
temp = 0
numlist = [[0 for _ in range(MAX)] for _ in range(MAX)]
maxlist = [0 for _ in range(MAX)]
plist = [0 for _ in range(MAX)]
qlist = [0 for _ in range(MAX)]
n, m = map(int, input().split())
for i in range(n):
    s = input()
    for j in range(m):
        if s[j] == 'R':
            numlist[i + 1][j + 1] = 1
for i in range(1, n + 1):
    p = q = Sum = 0
    for j in range(1, m + 1):
        if numlist[i][j] == 0:
            temp += i * j
            Sum = i * j
            maxlist[j] = plist[p] = i
            qlist[q] = j
            p += 1; q += 1
        else:
            while maxlist[j] > plist[p - 1] and p > 0:
                u = qlist[q - 2] if q > 1 else 0
                Sum -= (qlist[q - 1] - u) * plist[p - 1]
                p -= 1; q -= 1
            u = qlist[q - 1] if q > 0 else 0
            Sum += (j - u) * maxlist[j]
            plist[p], qlist[q] = maxlist[j], j
            temp += Sum
            p += 1; q += 1
print(n * (n + 1) // 2 * m * (m + 1) // 2 - temp)

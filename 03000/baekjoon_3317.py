cnt = [0 for _ in range(5)]
result = [0 for _ in range(5)]
a = [[[[0 for _ in range(37)] for _ in range(37)] for _ in range(37)] for _ in range(37)]
def toi(t):
    if 'a' <= t <= 'z':
        return ord(t) - 87
    return ord(t) - 48
def backtracking(x):
    if x == 4:
        p = a[pos[0]][pos[1]][pos[2]][pos[3]]
        l = 0
        for i in range(4):
            if pos[i] != 36:
                l += 1
        cnt[l] += p * (p - 1) // 2
        return
    for i in range(37):
        pos[x] = i
        backtracking(x + 1)
n, d = map(int, input().split())
for i in range(n):
    s = input()
    for j in range(16):
        pos = [0 for _ in range(4)]
        for k in range(4):
            if (j >> k) & 1:
                pos[k] = 36
            else:
                pos[k] = toi(s[k])
        a[pos[0]][pos[1]][pos[2]][pos[3]] += 1
pos = [0 for _ in range(4)]
backtracking(0)
result[3] = cnt[3]
result[2] = cnt[2] - 3 * result[3]
result[1] = cnt[1] - 2 * result[2] - 3 * result[3]
result[0] = n * (n - 1) // 2 - result[1] - result[2] - result[3]
print(result[4 - d])

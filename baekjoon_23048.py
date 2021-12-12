n = int(input())
seive = [0, 1] + [0] * (n - 1)
k = 1
for i in range(2, n + 1):
    if seive[i] == 0:
        k += 1
        seive[i] = k
        for j in range(i + i, n + 1, i):
            if seive[j] == 0:
                seive[j] = k
print(k)
print(*seive[1:])

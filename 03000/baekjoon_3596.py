n = int(input()) + 5
result = [0 for _ in range(n)]
for i in range(5, n):
    grundy = set()
    for j in range(3, i - 1):
        grundy.add(result[j - 1] ^ result[i - j])
    while result[i] in grundy:
        result[i] += 1
print(((result[-1] > 0) ^ 1) + 1)

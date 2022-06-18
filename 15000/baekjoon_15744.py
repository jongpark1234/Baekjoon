MOD = 1000000007
n = int(input())
result = 2 - n
divisions = []
for i in range(1, int(n ** 0.5) + 1):
    if n % i == 0:
        divisions += [i, n // i]
divisions.sort()
divisions.pop()
divisions = sorted(list(set(divisions)))
m = [1] + [0 for _ in range(len(divisions) - 1)]
for i in range(len(m)):
    for j in range(i + 1, len(m)):
        if divisions[j] % divisions[i] == 0:
            m[j] -= m[i]
for i in range(len(divisions)):
    for j in range(i, len(divisions)):
        if divisions[j] % divisions[i] == 0:
            result += pow(2, divisions[j] // divisions[i], MOD) * m[i] * ((n // divisions[j] - 1) % MOD) % MOD
            result %= MOD
print(result)

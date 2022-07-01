MOD = 1000000007
rp = [[0 for _ in range(101)] for _ in range(101)]
arr = [0 for _ in range(101)]
for i in range(101):
    rp[i][0] = 1
    for j in range(1, i + 1):
        rp[i][j] = (rp[i - 1][j] + rp[i - 1][j - 1]) % MOD
a, b, c, A, B, C = map(int, input().split())
if True not in map(bool, [A % a, B % b, C % c]):
    result = (((((((((((a * b * c + c * pow((pow(a, B // b, MOD) * b + pow(b, A // a, MOD) * a - a * b + MOD) % MOD, C // c, MOD)) % MOD) + b * pow((pow(a, C // c, MOD) * c + pow(c, A // a, MOD) * a - a * c + MOD) % MOD, B // b, MOD)) % MOD) + a * pow((pow(b, C // c, MOD) * c + pow(c, B // b, MOD) * b - b * c + MOD) % MOD, A // a, MOD)) % MOD) - a * b * pow(c, A // a * B // b, MOD) % MOD + MOD) % MOD) - b * c * pow(a, B // b * C // c, MOD) % MOD + MOD) % MOD) - a * c * pow(b, A // a * C // c, MOD) % MOD + MOD) % MOD
    for i in range(1, B // b):
        for j in range(A // a)[::-1]:
            arr[j] = rp[B // b][i] * rp[A // a][j] % MOD * pow(pow(c, A // a - j, MOD) - 1, B // b - i, MOD) % MOD
            for k in range(j + 1, A // a):
                arr[j] = (arr[j] - arr[k] * rp[k][j] + MOD) % MOD
            result = (result + arr[j] * (pow(pow(b, j, MOD) + pow(a, i, MOD) - 1, C // c, MOD) - pow(pow(b, j, MOD), C // c, MOD) - pow(pow(a, i, MOD), C // c, MOD) + 1) % MOD * a * b * c % MOD + MOD) % MOD
    print(result)
else:
    print(0)

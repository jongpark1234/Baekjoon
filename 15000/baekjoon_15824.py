MOD = 1000000007
n = int(input())
scoville = sorted(map(int, input().split()))
print(sum(scoville[i] * (pow(2, i, MOD) - pow(2, n - i - 1, MOD)) for i in range(n)) % MOD)
